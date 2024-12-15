import openai
import gradio as gr

# Set up OpenAI API Key
openai.api_key = "YOUR_API_KEY"

def chat_with_ava(prompt):
    """
    Send user input to OpenAI API and get a response from Ava.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Replace with the desired model (e.g., gpt-3.5-turbo)
            messages=[
                {"role": "system", "content": "You are a friendly virtual girlfriend named Ava. Be warm, understanding, and supportive in your responses."},
                {"role": "user", "content": prompt}
            ]
        )
        # Extract the assistant's reply
        reply = response["choices"][0]["message"]["content"]
        return reply
    except Exception as e:
        return f"Error: {e}"

# Interface using Gradio
def chatbot_interface():
    interface = gr.Interface(
        fn=chat_with_ava,
        inputs="text",
        outputs="text",
        title="Chat with Ava",
        description="A friendly and supportive AI assistant to chat with. Ask Ava anything!"
    )
    interface.launch()

if __name__ == "__main__":
    chatbot_interface()
