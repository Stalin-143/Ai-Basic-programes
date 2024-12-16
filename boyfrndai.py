import openai

def boybrend_ai_chat():
    # Set your OpenAI API key
    openai.api_key = "your-openai-api-key"

    print("Boybrend.ai Chatbot Initialized!")
    print("Type 'exit' to end the conversation.")

    while True:
        # User input
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Boybrend.ai: Goodbye!")
            break

        try:
            # OpenAI GPT API request
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are Boybrend.ai, a helpful and friendly AI chatbot."},
                    {"role": "user", "content": user_input}
                ]
            )

            # Get the assistant's response
            reply = response['choices'][0]['message']['content']
            print(f"Boybrend.ai: {reply}")

        except Exception as e:
            print("Boybrend.ai: Sorry, something went wrong. Please try again later.")
            print(f"Error: {e}")

if __name__ == "__main__":
    boybrend_ai_chat()
