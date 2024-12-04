import os
import requests


if __name__ == "__main__":
    token = os.environ["API_TOKEN"]
    chats_dir = "chats"
    chat_ids = os.listdir(chats_dir)
    chat_ids = [int(chat_id) for chat_id in chat_ids]
    message = "What are you doing right now?"
    for chat_id in chat_ids:
        url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        print(requests.get(url).json())
