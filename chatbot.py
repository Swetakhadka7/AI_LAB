def chatbot_response(user_input):
    responses = {
        "hello": "Hi, how can I help you?",
        "hi": "Hello! What can I do for you?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "what is your name": "I'm a simple chatbot created to assist you.",
        "bye": "Goodbye! Have a great day!"
    }

    # Convert input to lowercase to handle case insensitivity
    user_input = user_input.lower()

    # Check if input is in predefined responses
    return responses.get(user_input, "I'm not sure I understand. Can you rephrase?")

# Chat loop
while True:
    user_message = input("You: ")
    if user_message.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_message)
    print("Chatbot:", response)
