import requests

def send_to_slack(webhook, message):
    payload = {"text": f"🚨 *Sentinel Alert*\n{message}"}
    requests.post(webhook, json=payload)
