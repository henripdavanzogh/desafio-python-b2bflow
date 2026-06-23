from config import SUPABASE_URL, SUPABASE_KEY
from supabase import create_client
import logging

supabase = create_client(
    supabase_key=SUPABASE_KEY,
    supabase_url=SUPABASE_URL,
)


def get_contacts():
    table_contacts = supabase.table("Contatos").select("*").limit(3).execute()
    logging.info(f"{len(table_contacts.data)} contatos encontrados.")
    return table_contacts.data
