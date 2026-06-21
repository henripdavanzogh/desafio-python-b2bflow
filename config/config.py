from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    # supabase
    SUPABASE_API_URL = os.getenv("SUPABASE_API_URL")
    SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")

    # zapi
    ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
    ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")
