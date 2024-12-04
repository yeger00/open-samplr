import os
import requests


if __name__ == "__main__":
    token = os.environ["API_TOKEN"]
    chats_dir= "chats"
    chat_ids = os.listdir(chats_dir)
    chat_id_to_msgs = {int(chat_id): [] for chat_id in chat_ids}
    url = f"https://api.telegram.org/bot{token}/getUpdates"
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
