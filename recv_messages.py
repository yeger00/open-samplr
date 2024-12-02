import os
import requests

TOKEN = os.environ["API_TOKEN"]
CHATS_DIR = "chats"
chat_ids = os.listdir(CHATS_DIR)
chat_id_to_msgs = {int(chat_id): [] for chat_id in chat_ids}
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
result = requests.get(url).json()
if not result["ok"]:
    print("Failed to get result")
    print(result)
    exit(1)

for message in result["result"]:
    msg_chat_id = message["message"]["chat"]["id"]
    if msg_chat_id in chat_id_to_msgs:
        print("existing chat_id", msg_chat_id)
        chat_id_to_msgs[msg_chat_id].append(message["message"]["text"])
    else:
        print("New chat_id", msg_chat_id)
        chat_id_to_msgs[msg_chat_id] = []

for chat_id, messages in chat_id_to_msgs.items():
    with open(os.path.join(CHATS_DIR, str(chat_id)), "a") as f:
        f.write("\n".join(messages))
