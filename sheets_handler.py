import gspread
import os
import json
from datetime import datetime

# Configuration
SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(__file__), 'service_account.json')

def init_sheets():
    """Initializes the Google Sheets client."""
    if not os.path.exists(SERVICE_ACCOUNT_FILE):
        print("Warning: service_account.json not found. Google Sheets integration disabled.")
        return None

    try:
        gc = gspread.service_account(filename=SERVICE_ACCOUNT_FILE)
        return gc
    except Exception as e:
        print(f"Error initializing Google Sheets: {e}")
        return None

def append_invoice(order_data):
    """Appends invoice data to the configured Google Sheet."""
    sheet_id = os.environ.get('GOOGLE_SHEET_ID')
    if not sheet_id:
        print("Warning: GOOGLE_SHEET_ID not set. Skipping Sheets export.")
        return False

    gc = init_sheets()
    if not gc:
        return False

    try:
        sh = gc.open_by_key(sheet_id)
        worksheet = sh.sheet1  # Use the first sheet

        # Prepare row data
        # Headers (implied): ID, Date, Client, NIF, Email, Phone, Total, Status
        row = [
            order_data.get('invoice_id'),
            order_data.get('date'),
            order_data.get('client_name'),
            order_data.get('client_nif'),
            order_data.get('client_email'),
            order_data.get('client_phone'),
            order_data.get('total_general'),
            "Generated"
        ]
        
        # Append items details if needed, or just summary
        # For now, appending summary row
        worksheet.append_row(row)
        print(f"Successfully appended invoice {order_data.get('invoice_id')} to Google Sheet.")
        return True

    except Exception as e:
        print(f"Failed to append to Google Sheet: {e}")
        return False
