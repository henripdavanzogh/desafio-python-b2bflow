from dotenv import load_dotenv
import os

load_dotenv()
# supabase
SUPABASE_URL = os.getenv("SUPABASE_API_URL")
SUPABASE_KEY = os.getenv("SUPABASE_API_KEY")
# z-api
INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
TOKEN = os.getenv("ZAPI_INSTANCE_TOKEN")
CLIENT_TOKEN = os.getenv("ZAPI_CLIENT_TOKEN")

if not SUPABASE_URL:
    raise ValueError("SUPABASE_API_URL não configurada")
elif not SUPABASE_KEY:
    raise ValueError("SUPABASE_API_KEY não configurada")
elif not INSTANCE_ID:
    raise ValueError("ZAPI_INSTANCE_ID não configurada")
elif not TOKEN:
    raise ValueError("ZAPI_INSTANCE_TOKEN não configurada")
elif not CLIENT_TOKEN:
    raise ValueError("ZAPI_CLIENT_TOKEN não configurada")
