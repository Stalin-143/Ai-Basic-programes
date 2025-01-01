import random
import time

def new_year_greeting():
    greetings = [
        "Happy New Year! 🎉 May this year bring you joy and success!",
        "Wishing you a fantastic New Year filled with new opportunities! 🎆",
        "Cheers to a prosperous and exciting New Year! 🥂",
        "Happy 2025! Let's make it a year to remember! 🎇",
        "Here’s to new beginnings and endless possibilities. Happy New Year! 🌟",
    ]

    advice = [
        "Set meaningful goals and take small steps toward achieving them.",
        "Remember to celebrate your victories, big or small.",
        "Stay positive and embrace challenges as opportunities to grow.",
        "Prioritize your health and well-being in the coming year.",
        "Keep learning and exploring new things to expand your horizons.",
    ]

    print(random.choice(greetings))
    time.sleep(2)  # Adding a pause for effect
    print("\nHere's a New Year's tip for you:")
    print(random.choice(advice))

if __name__ == "__main__":
    print("Welcome to the New Year AI Bot! 🎊")
    time.sleep(1)
    print("\nLet me share a special message for you...\n")
    time.sleep(2)
    new_year_greeting()
