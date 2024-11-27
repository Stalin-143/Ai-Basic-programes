import nltk
from nltk.chat.util import Chat, reflections

# Define pairs for conversation patterns
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?", "Hi there! What can I do for you?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created to help you!", "You can call me ChatBot."]
    ],
    [
        r"how are you?",
        ["I'm just a bot, but I'm here to help!", "I'm doing well, thanks for asking!"]
    ],
    [
        r"can you help me with (.*)",
        ["Sure! I can help you with %1. Can you provide more details?", "Of course! Tell me more about %1."]
    ],
    [
        r"(.*) your favorite (.*)",
        ["I don't have preferences, but I enjoy assisting you!", "I don't have a favorite %2, but I love helping."]
    ],
    [
        r"(.*) (location|city)?",
        ["I'm a virtual assistant, so I exist in the cloud!"]
    ],
    [
        r"how (.*) work",
        ["I process information and respond based on patterns. It's like a virtual conversation!"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! Have a great day!", "Bye! Feel free to chat with me anytime."]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Can you rephrase?", "Interesting. Tell me more!"]
    ]
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Start the chatbot
def chatbot_interface():
    print("Hi, I'm ChatBot! Type 'quit' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'quit':
            print("ChatBot: Goodbye! Have a nice day!")
            break
        response = chatbot.respond(user_input)
        print("ChatBot:", response)

# Run the chatbot
if __name__ == "__main__":
    chatbot_interface()
