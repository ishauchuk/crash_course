short_messages = ['hi', 'hello', 'how are you?', "i'm fine", 'thank you']
sent_messages = []

def send_messages(short_messages):
    while short_messages:
        current_message = short_messages.pop()
        print(f"Message is: {current_message}")
        sent_messages.append(current_message)

send_messages(short_messages)
print(short_messages)
print(sent_messages)