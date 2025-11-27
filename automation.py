from datetime import datetime
from datetime import datetime
import supabase_db as database
import pdf_generator
import email_sender
import os

def process_order(form_data):
    # 1. Parse Form Data
    client_data = {
        'name': form_data.get('name'),
        'email': form_data.get('email'),
        'phone': form_data.get('phone'),
        'nif': form_data.get('nif'),
        'address': form_data.get('address'),
        'city': form_data.get('city'),
        'zip': form_data.get('zip')
    }

    items = []
    subtotal = 0.0
    
    # Process up to 6 products
    for i in range(1, 7):
        name = form_data.get(f'prod_name_{i}')
        if name:
            try:
                qty = int(form_data.get(f'prod_qty_{i}', 0))
                price = float(form_data.get(f'prod_price_{i}', 0.0))
                total = qty * price
                subtotal += total
                items.append({
                    'name': name,
                    'quantity': qty,
                    'price': price,
                    'total': total
                })
            except ValueError:
                continue

    iva_rate = 0.21
    iva_total = subtotal * iva_rate
    total_general = subtotal + iva_total

    # 2. Generate Invoice ID (Simple sequential for demo)
    # In a real app, we'd check the last ID in DB
    existing_dades = database.get_dades()
    next_id_num = len(existing_dades) + 1
    invoice_type = 'C' # Default to Comanda
    invoice_id = f"{invoice_type}-{next_id_num:05d}"

    order_data = {
        'invoice_id': invoice_id,
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'client_name': client_data['name'],
        'client_nif': client_data['nif'],
        'client_phone': client_data['phone'],
        'client_email': client_data['email'],
        'items': items,
        'subtotal': subtotal,
        'iva_total': iva_total,
        'total_general': total_general
    }

    # Step 2: Add to DADES
    database.add_dade(order_data)

    # Step 3: Generate PDF
    pdf_filename = pdf_generator.generate_invoice(order_data, invoice_id)
    pdf_path = os.path.join(pdf_generator.INVOICES_DIR, pdf_filename)

    # Step 9 (New): Send Email
    email_sender.send_invoice_email(
        to_email=client_data['email'],
        client_name=client_data['name'],
        invoice_filename=pdf_filename,
        invoice_path=pdf_path
    )

    # Step 10 (New): Add to Google Sheets
    import sheets_handler
    sheets_handler.append_invoice(order_data)

    # Step 6 & 7: Check Client
    existing_client = database.get_client_by_phone(client_data['phone'])
    
    if not existing_client:
        # Step 8: New Client
        new_client = client_data.copy()
        new_client['total_orders'] = 1
        new_client['total_spent'] = total_general
        new_client['first_seen'] = order_data['date']
        database.add_client(new_client)
    else:
        # Update stats
        database.update_client_stats(client_data['phone'], total_general)

    # Step 5: Add to COMANDES (Summary)
    summary = {
        'invoice_id': invoice_id,
        'date': order_data['date'],
        'client_name': client_data['name'],
        'total': total_general,
        'pdf_link': f"/invoices/{pdf_filename}",
        'status': 'Pending'
    }
    database.add_comanda(summary)

    return invoice_id, pdf_filename

def process_invoice_json(invoice_data):
    """
    Process invoice data received from the frontend (JSON).
    1. Save to DB (Supabase)
    2. Generate PDF
    3. Send Email
    """
    # Map frontend keys to DB keys if necessary
    # Frontend: client, nif, phone, email, address, city, postalCode, products, total, invoiceNumber
    
    # Ensure items have the correct structure
    items = []
    for p in invoice_data.get('products', []):
        items.append({
            'name': p.get('name'),
            'quantity': p.get('quantity'),
            'price': p.get('price'),
            'total': p.get('total')
        })

    # Prepare data for PDF generator and DB
    # Note: pdf_generator expects specific keys. We might need to adjust it or the data.
    # Let's look at pdf_generator.generate_invoice to see what it needs.
    # Assuming it needs 'invoice_id', 'date', 'client_name', 'items', 'subtotal', 'iva_total', 'total_general'
    
    # Calculate totals if not provided (though frontend sends them)
    # But let's trust frontend for now or recalculate? Better to use frontend values to match.
    
    db_entry = {
        'invoice_id': invoice_data.get('invoiceNumber'),
        'date': invoice_data.get('timestamp') or datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'client_name': invoice_data.get('client'),
        'client_nif': invoice_data.get('dni'),
        'client_phone': invoice_data.get('phone'),
        'client_email': invoice_data.get('email'),
        'client_address': invoice_data.get('address'),
        'client_city': invoice_data.get('city'),
        'client_zip': invoice_data.get('postalCode'),
        'items': items,
        'subtotal': invoice_data.get('subtotal'),
        'iva_total': invoice_data.get('iva'), # Frontend might call it 'ivaAmount' or just part of total
        'total_general': invoice_data.get('total'),
        'payment_method': invoice_data.get('paymentMethod'),
        'paid_status': invoice_data.get('paidStatus'),
        'delivery_date': invoice_data.get('deliveryDate'),
        'entry_date': invoice_data.get('entryDate')
    }
    
    # 1. Save to Supabase
    # Check if exists first? 
    # For now, just add. If ID exists, it might error or duplicate. 
    # Supabase 'invoices' table might have constraints.
    # Let's assume we want to save it.
    database.add_dade(db_entry)
    
    # 2. Generate PDF
    # We need to ensure pdf_generator works with this data structure.
    # If pdf_generator.generate_invoice expects the same structure as 'order_data' in process_order, we are good.
    # Let's verify pdf_generator.py in the next step if needed, but for now we pass db_entry.
    try:
        pdf_filename = pdf_generator.generate_invoice(db_entry, db_entry['invoice_id'])
        pdf_path = os.path.join(pdf_generator.INVOICES_DIR, pdf_filename)
        
        # 3. Send Email
        if db_entry['client_email']:
            email_sender.send_invoice_email(
                to_email=db_entry['client_email'],
                client_name=db_entry['client_name'],
                invoice_filename=pdf_filename,
                invoice_path=pdf_path
            )
            return {"status": "success", "message": "Invoice processed and email sent"}
        else:
            return {"status": "success", "message": "Invoice processed (no email provided)"}
            
    except Exception as e:
        print(f"Error processing invoice: {e}")
        return {"status": "error", "message": str(e)}
