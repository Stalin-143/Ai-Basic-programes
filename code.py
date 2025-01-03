import random

# New Year wishes and responses
new_year_responses = [
    "Happy New Year! 🎉 May this year bring you joy and success!",
    "Wishing you a fantastic New Year filled with amazing opportunities! 🥳",
    "Cheers to a new year and another chance to make dreams come true! 🍾",
    "Hope this New Year is full of exciting surprises and happiness! 🎆",
    "Here's to health, happiness, and prosperity in the New Year! 🌟",
]

# Fun New Year resolutions suggestions
resolutions = [
    "Start a gratitude journal. 📓",
    "Learn a new skill or hobby. 🎸",
    "Exercise regularly and stay fit. 🏋️‍♂️",
    "Travel to a new place you've never been. ✈️",
    "Spend more quality time with family and friends. ❤️",
]

def chatbot():
    print("🎉 Welcome to the New Year Special Chatbot! 🎉")
    print("Type 'quit' to exit the chat.\n")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "quit":
            print("Chatbot: Goodbye! Wishing you a wonderful New Year! 🎊")
            break
        elif "new year" in user_input:
            print(f"Chatbot: {random.choice(new_year_responses)}")
        elif "resolution" in user_input or "suggest" in user_input:
            print(f"Chatbot: How about this resolution? {random.choice(resolutions)}")
        else:
            print("Chatbot: That's great! Let's make this New Year amazing together. 🌟")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
