import os
import requests


TOKEN = os.environ["API_TOKEN"]
CHATS_DIR = "chats"
chat_ids = os.listdir(CHATS_DIR)
chat_ids = [int(chat_id) for chat_id in chat_ids]
message = "What are you doing right now?"
for chat_id in chat_ids:
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json())
