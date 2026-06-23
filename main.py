from dotenv import load_dotenv
from services.supabase_client import get_contacts
from services.zapi_client import send_message

load_dotenv()

table_contacts = get_contacts()
for contact in table_contacts:
    send_message(contact["nome"], contact["telefone"])
