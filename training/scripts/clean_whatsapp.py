import re
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

env_names = os.getenv("ASSISTANT_NAMES", "")
ASSISTANT_NAMES = [name.strip() for name in env_names.split(",") if name.strip()]

print(f"Using assistant names: {ASSISTANT_NAMES}")

def clean_whatsapp_file(input_file_path, output_file_path, assistant_names=["Balbi", "Manasés", "Luis Miguel"]):
    """
    Parses a Whatsapp .txt export and formats it into a JSONL file
    compatible with OpenAI/Unsloth chat templates.
    """
    # Pattern to match 08/01/26, 1:25 pm - Name: Message
    # This handles both names and phone numbers as the sender
    pattern = re.compile(r"^(\d{2}/\d{2}/\d{2},\s\d{1,2}:\d{2}\s(?:am|pm))\s-\s(.*?):\s(.*)")

    chat_history = []

    if not os.path.exists(input_file_path):
        print(f"File not found: {input_file_path}")
        return
    
    with open(input_file_path, "r", encoding="utf-8") as file:
        for line in file:
            # Try to match the message pattern
            match = pattern.match(line.strip())

            # If if doesn't match (admin action, media omitted, etc.), just skip it
            if not match:
                continue

            sender = match.group(2).strip()
            message = match.group(3).strip()

            # Skip specific WhatsApp media placeholders if they matched the pattern
            if "<Media omitted>" in message or "This message was deleted" in message:
                continue

            role = "assistant" if sender in assistant_names else "user"

            # Context: Prepend name for users so model knows who is talking
            content = f"{sender}: {message}" if role == "user" else message
            chat_history.append({
                "role": role,
                "content": content
            })

        # Create sliding windows of 6 messages
        dataset = []

        for i in range(len(chat_history) - 6):
            window = chat_history[i : i + 6]
            # Only learn from the assistant's specific humor
            if window[-1]["role"] == "assistant":
                dataset.append({"messages": window})

        with open(output_file_path, "w", encoding="utf-8") as outfile:
            for entry in dataset:
                outfile.write(json.dumps(entry, ensure_ascii=False) + '\n')

        print(f"Processed {len(dataset)} chat windows into {output_file_path}.")

if __name__ == "__main__":
    input_path = "training/data/WhatsApp Chat.txt"
    output_path = "training/data/whatsapp_chat_cleaned.jsonl"
    clean_whatsapp_file(input_path, output_path, ASSISTANT_NAMES)
