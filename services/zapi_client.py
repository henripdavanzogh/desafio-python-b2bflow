import logging

import requests
from config import INSTANCE_ID, TOKEN, CLIENT_TOKEN

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def send_message(name, phone):
    try:
        message = f"Olá, {name} tudo bem com você?"

        # data
        url = f"https://api.z-api.io/instances/{INSTANCE_ID}/token/{TOKEN}/send-text"
        payload = {"phone": phone, "message": message}
        headers = {"Client-Token": CLIENT_TOKEN}
        response = requests.post(
            url=url, json=payload, headers=headers, timeout=5
        )
        if response.ok:
            logging.info(f"Mensagem enviada para {name}")
        elif response.status_code in (400, 405):
            logging.error(
                f"Erro na requisição: ({response.status_code}) -  {response.text}"
            )
        elif response.status_code == 415:
            logging.error("Header: Content-Type não informado")
        elif response.status_code >= 500:
            logging.error(f"Erro na API: {response.text}")
        else:
            logging.error(
                f"Erro inesperado: {response.status_code} - {response.text}"
            )

    except requests.RequestException as error:
        logging.info(f"Erro ao enviar mensagem: {error}")
