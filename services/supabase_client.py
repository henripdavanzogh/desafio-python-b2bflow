from config import SUPABASE_URL, SUPABASE_KEY
from supabase import create_client

supabase = create_client(
    supabase_key=SUPABASE_KEY,
    supabase_url=SUPABASE_URL,
)


def get_contacts():
    table_contacts = supabase.table("contacts").select("*").limit(3).execute()
    # treat the errors on zapi_client.py
    return table_contacts.data
