from dotenv import load_dotenv
from supabase import create_client
from config import SUPABASE_URL, SUPABASE_API_URL

load_dotenv()

supabase = create_client(
    supabase_key=SUPABASE_URL,
    supabase_url=SUPABASE_API_URL,
)

response = supabase.table("contatos").select("*").execute()
print(response.data)
