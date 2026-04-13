import requests
import os
from dotenv import load_dotenv

load_dotenv()

webhook_url = os.getenv("secret_webhook")


def send_discord_message(message):
    package = {
        "content": message
    }

    
    try: 
        answer = requests.post(webhook_url, json=package)

        if answer.status_code == 204:
            return True
        else:
            return False
    except Exception as e:
        return False
    


