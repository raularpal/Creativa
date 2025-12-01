import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load env vars if not already loaded
load_dotenv()

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

def get_client() -> Client:
    if not SUPABASE_URL or not SUPABASE_KEY:
        print("Error: Supabase credentials not found.")
        return None
    return create_client(SUPABASE_URL, SUPABASE_KEY)

def init_db():
    # No local init needed for Supabase
    pass

def get_dades():
    # "Dades" in the original code seems to be the list of all orders/invoices
    # We'll fetch from 'invoices' table
    supabase = get_client()
    if not supabase: return []
    try:
        response = supabase.table("invoices").select("*").execute()
        return response.data
    except Exception as e:
        print(f"Error fetching dades: {e}")
        return []

def add_dade(entry):
    supabase = get_client()
    if not supabase: return
    try:
        # Ensure items is JSON serializable if not handled automatically
        # Supabase-py handles dicts as JSONB
        supabase.table("invoices").insert(entry).execute()
    except Exception as e:
        print(f"Error adding dade: {e}")

def get_clients():
    supabase = get_client()
    if not supabase: return []
    try:
        response = supabase.table("clients").select("*").execute()
        return response.data
    except Exception as e:
        print(f"Error fetching clients: {e}")
        return []

def get_client_by_phone(phone):
    supabase = get_client()
    if not supabase: return None
    try:
        response = supabase.table("clients").select("*").eq("phone", phone).execute()
        if response.data:
            return response.data[0]
        return None
    except Exception as e:
        print(f"Error fetching client by phone: {e}")
        return None

def add_client(client_data):
    supabase = get_client()
    if not supabase: return
    try:
        supabase.table("clients").insert(client_data).execute()
    except Exception as e:
        print(f"Error adding client: {e}")

def update_client_stats(phone, amount):
    supabase = get_client()
    if not supabase: return
    try:
        # First get current stats
        client = get_client_by_phone(phone)
        if client:
            new_orders = (client.get('total_orders') or 0) + 1
            new_spent = float(client.get('total_spent') or 0.0) + float(amount)
            
            supabase.table("clients").update({
                "total_orders": new_orders,
                "total_spent": new_spent
            }).eq("phone", phone).execute()
    except Exception as e:
        print(f"Error updating client stats: {e}")

def add_comanda(summary):
    # In the original code, 'comandes' was a summary list.
    # In Supabase, we might just query the invoices table for summaries.
    # But to keep compatibility, we can either ignore this if we use 'invoices' for everything,
    # or we can have a separate 'comandes' table.
    # Looking at automation.py, 'add_dade' adds the full order data, and 'add_comanda' adds a summary.
    # Let's assume we just use the 'invoices' table for everything and 'get_comandes' returns a simplified view.
    # For now, let's just do nothing or log it, assuming 'invoices' table holds the truth.
    # Actually, let's check if 'add_dade' and 'add_comanda' are redundant in the new design.
    # 'add_dade' saves full data. 'add_comanda' saves summary.
    # We can just use 'invoices' table.
    pass

def get_comandes():
    # Return list of invoices, maybe simplified
    return get_dades()

def get_counters():
    # We can store counters in a separate table or just count rows.
    # For simplicity, let's return a static dict or query DB count.
    # The original code stored counters for invoice IDs.
    # We are generating IDs based on list length in automation.py.
    # We should probably change ID generation to be DB-based or count rows.
    supabase = get_client()
    if not supabase: return {"Comanda": 0}
    try:
        count = supabase.table("invoices").select("*", count="exact").execute().count
        return {"Comanda": count}
    except:
        return {"Comanda": 0}

def save_counters(counters):
    # Not needed if we calculate dynamically
    pass

def save_invoice(invoice):
    # This seems redundant with add_dade in original code?
    # automation.py calls add_dade. app.py calls save_invoice.
    # Let's map it to add_dade.
    add_dade(invoice)

def get_invoices():
    return get_dades()
