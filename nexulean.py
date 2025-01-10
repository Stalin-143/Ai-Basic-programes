from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = Flask(__name__)

# Load the AI model and tokenizer
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Initialize chat history
chat_history_ids = None
def reset_chat_history():
    global chat_history_ids
    chat_history_ids = None

@app.route("/chat", methods=["POST"])
def chat():
    global chat_history_ids

    # Get user input from the request
    user_input = request.json.get("message", "")

    if not user_input:
        return jsonify({"error": "Message is required"}), 400

    try:
        # Tokenize user input
        input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")

        # Generate a response
        chat_history_ids = model.generate(
            input_ids if chat_history_ids is None else torch.cat([chat_history_ids, input_ids], dim=-1),
            max_length=1000,
            pad_token_id=tokenizer.eos_token_id,
        )

        # Decode the response
        response = tokenizer.decode(chat_history_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/reset", methods=["POST"])
def reset():
    reset_chat_history()
    return jsonify({"message": "Chat history reset successfully."})

@app.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "Chatbot is running", "model": model_name})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
