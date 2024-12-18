import requests
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import wikipedia

# Load the CLIP model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

def recognize_object(image_path):
    """Recognize objects in an image using CLIP."""
    image = Image.open(image_path)
    text_inputs = [
        "a painting", "a building", "a sculpture", "a park",
        "an animal", "a historic site", "a famous landmark"
    ]

    inputs = processor(text=text_inputs, images=image, return_tensors="pt", padding=True)
    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image
    probs = logits_per_image.softmax(dim=1)

    # Get the most probable label
    recognized_index = probs.argmax().item()
    recognized_label = text_inputs[recognized_index]
    confidence = probs[0, recognized_index].item()

    return recognized_label, confidence

def fetch_information(query):
    """Fetch a summary of information from Wikipedia."""
    try:
        summary = wikipedia.summary(query, sentences=2)
    except wikipedia.DisambiguationError as e:
        summary = f"Multiple results found: {e.options[:3]}..."
    except wikipedia.PageError:
        summary = "No relevant information found."
    return summary

if __name__ == "__main__":
    # Example image
    image_path = "example.jpg"  # Replace with your image file

    print("Recognizing object in the image...")
    label, confidence = recognize_object(image_path)
    print(f"Recognized as: {label} (Confidence: {confidence:.2f})")

    print("Fetching information...")
    description = fetch_information(label)
    print(f"Description: {description}")
