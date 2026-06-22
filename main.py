from dotenv import load_dotenv
from supabase import create_client
import os
import requests

load_dotenv()


# SUPABASE
def get_contacts():
    supabase = create_client(
        supabase_key=os.getenv("SUPABASE_API_KEY"),
        supabase_url=os.getenv("SUPABASE_API_URL"),
    )

    response = supabase.table("contatos").select("*").limit(3).execute()
    return response.data


# ZAPI
def send_message(name, phone):
    message = f"Olá, {name} tudo bem com você?"

    INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
    TOKEN = os.getenv("ZAPI_INSTANCE_TOKEN")
    CLIENT_TOKEN = os.getenv("ZAPI_CLIENT_TOKEN")

    # request data
    url = f"https://api.z-api.io/instances/{INSTANCE_ID}/token/{TOKEN}/send-text"
    payload = {"phone": phone, "message": message}
    headers = {"Client-Token": CLIENT_TOKEN}
    requests.post(url=url, json=payload, headers=headers)


table_contacts = get_contacts()
for contact in table_contacts:
    send_message((contact["name"], contact["phone_number"]))


if __name__ == "__main__":
    get_contacts()
