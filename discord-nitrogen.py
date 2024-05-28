import requests
import string
import random
import time

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1209889330613583903/D6h-osBtvxPH_ghNSkz50SqLiaDhNb6Wq1nUJSTT1WBRWfrhkCURfoW47I8IEoOvgb_4"

def generate_random_string(length=18):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def send_request_and_notify(code):
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    response = requests.get(url)
    if response.status_code == 200:
        print("Çalışan Bir Nitro Kodu Bulundu. 'disord.gift/code' şeklinde kullanarak discord nitronu alabilirsin")
        send_to_discord(code)

def send_to_discord(message):
    """Send a message to Discord through webhook."""
    payload = {"content": message}
    requests.post(DISCORD_WEBHOOK_URL, json=payload)

if __name__ == "__main__":
    while True:
        generated_string = generate_random_string()
        send_request_and_notify(generated_string)
        time.sleep(0.2)