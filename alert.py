import requests

def send_discord_message(message, webhook_url):
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
    


