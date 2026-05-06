def get_bot_reply(user_message):
    """
    Returns bot reply based on user input using if-elif rules.
    """
    user_message = user_message.lower().strip()

    if user_message in ["hi", "hello"]:
        return "Hi!"
    elif user_message == "how are you":
        return "I'm fine, thanks!"
    elif user_message == "bye":
        return "Goodbye! Have a great day!"
    elif user_message == "thanks":
        return "You're welcome!"
    else:
        return "Sorry, I don't understand that."


def run_chatbot():
    """
    Runs chatbot conversation in a loop until user says 'bye'.
    """
    print("=== Basic Rule-Based Chatbot ===")
    print("Type: hello/hi, how are you, bye, thanks")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        reply = get_bot_reply(user_input)
        print("Bot:", reply)

        if user_input.lower().strip() == "bye":
            break


if __name__ == "__main__":
    run_chatbot()