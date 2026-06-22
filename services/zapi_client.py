import requests
from config import INSTANCE_ID, TOKEN, CLIENT_TOKEN


def send_message(name, phone):
    message = f"Olá, {name} tudo bem com você?"

    # data
    url = (
        f"https://api.z-api.io/instances/{INSTANCE_ID}/token/{TOKEN}/send-text"
    )
    payload = {"phone": phone, "message": message}
    headers = {"Client-Token": CLIENT_TOKEN}
    response = requests.post(url=url, json=payload, headers=headers, timeout=5)

    # treat the errors on zapi_client.py
    if response.status_code == 200:
        print(f"Mensagem enviada para {name}")
    else:
        print(f"Erro ao enviar mensagem para {name}")
