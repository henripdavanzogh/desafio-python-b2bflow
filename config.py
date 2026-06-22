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
