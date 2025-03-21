from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Dict, Tuple, Optional
import time  # Import time for timestamp

# Import the HybridRecommender class from BlazeTrail.py
from BlazeTrail import HybridRecommender

app = Flask(__name__)

# Initialize the recommender system
recommender = HybridRecommender()

# Load the full dataset from BlazeTrail.py
ratings_data = [
    # User 1
    {"user_id": "user1", "item_id": "movie1", "rating": 5.0},
    {"user_id": "user1", "item_id": "movie2", "rating": 4.0},
    {"user_id": "user1", "item_id": "movie3", "rating": 2.5},
    {"user_id": "user1", "item_id": "movie8", "rating": 4.2},
    {"user_id": "user1", "item_id": "movie12", "rating": 3.7},

    # User 2
    {"user_id": "user2", "item_id": "movie1", "rating": 4.5},
    {"user_id": "user2", "item_id": "movie4", "rating": 4.0},
    {"user_id": "user2", "item_id": "movie5", "rating": 3.5},
    {"user_id": "user2", "item_id": "movie9", "rating": 4.8},
    {"user_id": "user2", "item_id": "movie15", "rating": 2.3},

    # User 3
    {"user_id": "user3", "item_id": "movie2", "rating": 4.0},
    {"user_id": "user3", "item_id": "movie4", "rating": 5.0},
    {"user_id": "user3", "item_id": "movie6", "rating": 4.5},
    {"user_id": "user3", "item_id": "movie10", "rating": 3.9},
    {"user_id": "user3", "item_id": "movie14", "rating": 4.2},

    # User 4
    {"user_id": "user4", "item_id": "movie1", "rating": 3.5},
    {"user_id": "user4", "item_id": "movie3", "rating": 4.0},
    {"user_id": "user4", "item_id": "movie5", "rating": 3.0},
    {"user_id": "user4", "item_id": "movie7", "rating": 4.5},
    {"user_id": "user4", "item_id": "movie11", "rating": 5.0},

    # User 5
    {"user_id": "user5", "item_id": "movie2", "rating": 3.5},
    {"user_id": "user5", "item_id": "movie6", "rating": 4.0},
    {"user_id": "user5", "item_id": "movie8", "rating": 5.0},
    {"user_id": "user5", "item_id": "movie13", "rating": 3.8},
    {"user_id": "user5", "item_id": "movie16", "rating": 4.1},

    # User 6
    {"user_id": "user6", "item_id": "movie3", "rating": 4.2},
    {"user_id": "user6", "item_id": "movie7", "rating": 3.9},
    {"user_id": "user6", "item_id": "movie12", "rating": 4.7},
    {"user_id": "user6", "item_id": "movie17", "rating": 3.5},
    {"user_id": "user6", "item_id": "movie21", "rating": 4.0},

    # User 7
    {"user_id": "user7", "item_id": "movie4", "rating": 3.8},
    {"user_id": "user7", "item_id": "movie8", "rating": 4.3},
    {"user_id": "user7", "item_id": "movie13", "rating": 3.7},
    {"user_id": "user7", "item_id": "movie18", "rating": 4.9},
    {"user_id": "user7", "item_id": "movie22", "rating": 3.4},

    # User 8
    {"user_id": "user8", "item_id": "movie5", "rating": 4.1},
    {"user_id": "user8", "item_id": "movie9", "rating": 3.6},
    {"user_id": "user8", "item_id": "movie14", "rating": 4.5},
    {"user_id": "user8", "item_id": "movie19", "rating": 3.2},
    {"user_id": "user8", "item_id": "movie23", "rating": 4.8},

    # User 9
    {"user_id": "user9", "item_id": "movie6", "rating": 3.9},
    {"user_id": "user9", "item_id": "movie10", "rating": 4.4},
    {"user_id": "user9", "item_id": "movie15", "rating": 3.3},
    {"user_id": "user9", "item_id": "movie20", "rating": 4.7},
    {"user_id": "user9", "item_id": "movie24", "rating": 3.5},

    # User 10
    {"user_id": "user10", "item_id": "movie1", "rating": 4.2},
    {"user_id": "user10", "item_id": "movie7", "rating": 3.7},
    {"user_id": "user10", "item_id": "movie11", "rating": 4.6},
    {"user_id": "user10", "item_id": "movie16", "rating": 3.4},
    {"user_id": "user10", "item_id": "movie25", "rating": 4.3},

    # Users 11-20 (fewer ratings per user)
    {"user_id": "user11", "item_id": "movie2", "rating": 3.8},
    {"user_id": "user11", "item_id": "movie12", "rating": 4.1},
    {"user_id": "user11", "item_id": "movie22", "rating": 3.6},

    {"user_id": "user12", "item_id": "movie3", "rating": 4.3},
    {"user_id": "user12", "item_id": "movie13", "rating": 3.2},
    {"user_id": "user12", "item_id": "movie23", "rating": 4.5},

    {"user_id": "user13", "item_id": "movie4", "rating": 3.9},
    {"user_id": "user13", "item_id": "movie14", "rating": 4.7},
    {"user_id": "user13", "item_id": "movie24", "rating": 3.4},

    {"user_id": "user14", "item_id": "movie5", "rating": 4.4},
    {"user_id": "user14", "item_id": "movie15", "rating": 3.1},
    {"user_id": "user14", "item_id": "movie25", "rating": 4.6},

    {"user_id": "user15", "item_id": "movie6", "rating": 3.7},
    {"user_id": "user15", "item_id": "movie16", "rating": 4.2},
    {"user_id": "user15", "item_id": "movie26", "rating": 3.8},

    {"user_id": "user16", "item_id": "movie7", "rating": 4.5},
    {"user_id": "user16", "item_id": "movie17", "rating": 3.3},
    {"user_id": "user16", "item_id": "movie27", "rating": 4.1},

    {"user_id": "user17", "item_id": "movie8", "rating": 3.6},
    {"user_id": "user17", "item_id": "movie18", "rating": 4.8},
    {"user_id": "user17", "item_id": "movie28", "rating": 3.5},

    {"user_id": "user18", "item_id": "movie9", "rating": 4.0},
    {"user_id": "user18", "item_id": "movie19", "rating": 3.9},
    {"user_id": "user18", "item_id": "movie29", "rating": 4.3},

    {"user_id": "user19", "item_id": "movie10", "rating": 3.4},
    {"user_id": "user19", "item_id": "movie20", "rating": 4.6},
    {"user_id": "user19", "item_id": "movie30", "rating": 3.7},

    {"user_id": "user20", "item_id": "movie1", "rating": 4.2},
    {"user_id": "user20", "item_id": "movie11", "rating": 3.5},
    {"user_id": "user20", "item_id": "movie21", "rating": 4.4},
]

item_features = [
        {"item_id": "movie1", "title": "The Matrix", "features": "sci-fi action cyberpunk dystopian future AI virtual-reality"},
        {"item_id": "movie2", "title": "Nanban", "features": "comedy drama friendship college life love"},
        {"item_id": "movie3", "title": "The Godfather", "features": "crime drama mafia family power revenge classic"},
        {"item_id": "movie4", "title": "Natpe Thunai", "features": "comedy drama sport intresting "},
        {"item_id": "movie5", "title": "The Dark Knight", "features": "superhero action crime thriller batman joker"},
        {"item_id": "movie6", "title": "Blade Runner 2049", "features": "sci-fi dystopian future AI cyberpunk noir detective"},
        {"item_id": "movie7", "title": "leo", "features": "action gangster one person army action thriller crime"},
        {"item_id": "movie8", "title": "Avatar", "features": "sci-fi action adventure space aliens nature environment"},
        {"item_id": "movie9", "title": "The Shawshank Redemption", "features": "drama prison friendship hope redemption escape"},
        {"item_id": "movie10", "title": "The Lord of the Rings", "features": "fantasy adventure epic quest magic elves dwarves"},
        {"item_id": "movie11", "title": "Chennai 600028 ", "features": "drama comedy romance sport"},
        {"item_id": "movie12", "title": "Forrest Gump", "features": "drama comedy historical love friendship simplicity"},
        {"item_id": "movie13", "title": "The Silence of the Lambs", "features": "thriller crime psychological horror serial-killer fbi"},
        {"item_id": "movie14", "title": "Star Wars", "features": "sci-fi space opera adventure heroes villains force"},
        {"item_id": "movie15", "title": "Jurassic Park", "features": "sci-fi adventure dinosaurs genetic-engineering theme-park"},
        {"item_id": "movie16", "title": "Titanic", "features": "romance drama disaster historical ship tragedy"},
        {"item_id": "movie17", "title": "The Greatest Of All Time", "features": "action thriller one person army action "},
        {"item_id": "movie18", "title": "The Avengers", "features": "superhero action adventure team marvel aliens"},
        {"item_id": "movie19", "title": "The Lion King", "features": "animation family drama adventure coming-of-age animals"},
        {"item_id": "movie20", "title": "The Departed", "features": "crime thriller drama undercover police mafia identity"},
        {"item_id": "movie21", "title": "The Conjuring", "features": "horror mystery suspense mystery thriller supernatural horror "},
        {"item_id": "movie22", "title": "The Social Network", "features": "drama biography technology facebook startup betrayal"},
        {"item_id": "movie23", "title": "Back to the Future", "features": "sci-fi comedy adventure time-travel 1980s 1950s"},
        {"item_id": "movie24", "title": "Amaran", "features": "action epic tragedy action biography drama war army"},
        {"item_id": "movie25", "title": "The Revenant", "features": "adventure drama survival wilderness revenge bear"},
        {"item_id": "movie26", "title": "Hit The First Case", "features": " police procedural thriller crime drama mystery"},
        {"item_id": "movie27", "title": "Maattrraan", "features": "action sci-fi thriller conspiracy thriller"},
        {"item_id": "movie28", "title": "Eternal Sunshine of the Spotless Mind", "features": "romance drama sci-fi memory relationships technology"},
        {"item_id": "movie29", "title": "Darshana", "features": "upcoming movie scf-fi Horror  Mystery "},
        {"item_id": "movie30", "title": "La La Land", "features": "musical romance drama jazz hollywood dreams"},
        {"item_id": "movie31", "title": "Kaavalan", "features": "slapstick action comedy drama romance"},
        {"item_id": "movie32", "title": "chaarulatha", "features": "horror thriller twin sister love"},
        {"item_id": "movie33", "title": "Abina sri", "features": "kindfull mystery action love"},
        {"item_id": "movie34", "title": "Maharaja", "features": "crime drama one-person army action action thriller "},
        {"item_id": "movie35", "title": "Manjummel Boys", "features": "adventure drama thriller friendship"},
        {"item_id": "movie36", "title": "Premalu", "features": "comedy romance fun intresting action"},
        {"item_id": "movie37", "title": "Vikram", "features": "gun fu one-person army action crime thriller action"},
        {"item_id": "movie38", "title": "K.G.F", "features": "action epic gangster period drama crime thriller love "},
        {"item_id": "movie39", "title": "Stalin", "features": "hacker kindfull gangster"},
        {"item_id": "movie40", "title": "Comali", "features": "comedy memory loss love action drama"},
        {"item_id": "movie41", "title": "Miruthan", "features": "zombie horror action adventure sci-fi horror crime"},
        {"item_id": "movie42", "title": "Tik Tik Tik", "features": "action adventure sci-fi space travel love"},
        {"item_id": "movie43", "title": "Ayalaan", "features": "action adventure sci-fi alien"},
        {"item_id": "movie44", "title": "Joe", "features": "drama love action adventure comedy"},
        {"item_id": "movie45", "title": "Por Thozhil", "features": "action crime thriller love investigation"},
        {"item_id": "movie46", "title": "chithha", "features": "drama thriller love comedy action"},
        {"item_id": "movie47", "title": "viduthalai", "features": "action thriller crime drama "},
        {"item_id": "movie48", "title": "Teddy", "features": "action love fantasy adventure thriller"},
        {"item_id": "movie49", "title": "Sarpatta parambarai", "features": "boxing action drama sport love"},
        {"item_id": "movie50", "title": "Pariyerum Perumal", "features": "drama love action adve"},
        {"item_id": "movie51", "title": "Soorarai Pottru", "features": "drama hardwork action love thriller "},
        {"item_id": "movie52", "title": "Asuran", "features": "drama action period drama one-person army action"},
        {"item_id": "movie53", "title": "Raatchasan", "features": "psychological thriller serial killer suspense mystery crime thriller"},
        {"item_id": "movie54", "title": "Jai Bhim", "features": "legal drama crime drama"},
        {"item_id": "movie55", "title": "Kaithi", "features": "cop drama drug crime action crime thriller "},
        {"item_id": "movie56", "title": "12th Fail", "features": " docudrama biography drama "},
        {"item_id": "movie57", "title": "3 idiots", "features": "buddy comedy coming-of-age drama quirky comedy"},
        {"item_id": "movie58", "title": "Vikram Vedha", "features": "action crime drama thriller"},
        {"item_id": "movie59", "title": "Bahubali", "features": "action epic one-person army action drama"},
        {"item_id": "movie60", "title": "Friends", "features": "action comedy drama romance"}
    ]
    

social_connections = [
    {"user_id": "user1", "friend_id": "user2", "weight": 0.8},
    {"user_id": "user1", "friend_id": "user4", "weight": 0.6},
    {"user_id": "user1", "friend_id": "user10", "weight": 0.7},
    {"user_id": "user1", "friend_id": "user15", "weight": 0.4},

    {"user_id": "user2", "friend_id": "user3", "weight": 0.9},
    {"user_id": "user2", "friend_id": "user5", "weight": 0.5},
    {"user_id": "user2", "friend_id": "user7", "weight": 0.6},
    {"user_id": "user2", "friend_id": "user12", "weight": 0.7},

    {"user_id": "user3", "friend_id": "user5", "weight": 0.7},
    {"user_id": "user3", "friend_id": "user8", "weight": 0.8},
    {"user_id": "user3", "friend_id": "user13", "weight": 0.6},
    {"user_id": "user3", "friend_id": "user16", "weight": 0.5},

    {"user_id": "user4", "friend_id": "user5", "weight": 0.6},
    {"user_id": "user4", "friend_id": "user9", "weight": 0.7},
    {"user_id": "user4", "friend_id": "user14", "weight": 0.5},
    {"user_id": "user4", "friend_id": "user17", "weight": 0.4},

    {"user_id": "user5", "friend_id": "user6", "weight": 0.8},
    {"user_id": "user5", "friend_id": "user10", "weight": 0.7},
    {"user_id": "user5", "friend_id": "user15", "weight": 0.6},
    {"user_id": "user5", "friend_id": "user18", "weight": 0.5},

    {"user_id": "user6", "friend_id": "user7", "weight": 0.7},
    {"user_id": "user6", "friend_id": "user11", "weight": 0.6},
    {"user_id": "user6", "friend_id": "user16", "weight": 0.5},
    {"user_id": "user6", "friend_id": "user19", "weight": 0.4},

    {"user_id": "user7", "friend_id": "user8", "weight": 0.8},
    {"user_id": "user7", "friend_id": "user12", "weight": 0.7},
    {"user_id": "user7", "friend_id": "user17", "weight": 0.6},
    {"user_id": "user7", "friend_id": "user20", "weight": 0.5},

    {"user_id": "user8", "friend_id": "user9", "weight": 0.7},
    {"user_id": "user8", "friend_id": "user13", "weight": 0.6},
    {"user_id": "user8", "friend_id": "user18", "weight": 0.5},

    {"user_id": "user9", "friend_id": "user10", "weight": 0.8},
    {"user_id": "user9", "friend_id": "user14", "weight": 0.7},
    {"user_id": "user9", "friend_id": "user19", "weight": 0.6},

    {"user_id": "user10", "friend_id": "user15", "weight": 0.7},
    {"user_id": "user10", "friend_id": "user20", "weight": 0.6},

    {"user_id": "user11", "friend_id": "user12", "weight": 0.8},
    {"user_id": "user11", "friend_id": "user16", "weight": 0.7},

    {"user_id": "user12", "friend_id": "user13", "weight": 0.7},
    {"user_id": "user12", "friend_id": "user17", "weight": 0.6},

    {"user_id": "user13", "friend_id": "user14", "weight": 0.8},
    {"user_id": "user13", "friend_id": "user18", "weight": 0.7},

    {"user_id": "user14", "friend_id": "user15", "weight": 0.7},
    {"user_id": "user14", "friend_id": "user19", "weight": 0.6},

    {"user_id": "user15", "friend_id": "user16", "weight": 0.8},
    {"user_id": "user15", "friend_id": "user20", "weight": 0.7},

    {"user_id": "user16", "friend_id": "user17", "weight": 0.7},

    {"user_id": "user17", "friend_id": "user18", "weight": 0.8},

    {"user_id": "user18", "friend_id": "user19", "weight": 0.7},

    {"user_id": "user19", "friend_id": "user20", "weight": 0.8},
]

# Load data into the recommender
recommender.load_ratings_data(ratings_data)
recommender.load_item_features(item_features)
recommender.load_social_graph(social_connections)

@app.route('/')
def home():
    return render_template('index.html')  # Create an HTML template for the frontend

@app.route('/recommend', methods=['POST'])
def recommend():
    """
    API endpoint to get recommendations for a user.
    """
    data = request.json
    user_id = data.get('user_id')
    top_n = data.get('top_n', 5)  # Default to 5 recommendations

    if not user_id:
        return jsonify({"error": "user_id is required"}), 400

    recommendations = recommender.get_recommendations(user_id, top_n=top_n)
    return jsonify(recommendations)

@app.route('/explain', methods=['POST'])
def explain():
    """
    API endpoint to explain a recommendation for a user.
    """
    data = request.json
    user_id = data.get('user_id')
    item_id = data.get('item_id')

    if not user_id or not item_id:
        return jsonify({"error": "user_id and item_id are required"}), 400

    explanation = recommender.explain_recommendation(user_id, item_id)
    return jsonify(explanation)

@app.route('/visualize', methods=['POST'])
def visualize():
    """
    API endpoint to visualize the social graph for a user.
    """
    data = request.json
    user_id = data.get('user_id')

    if not user_id:
        return jsonify({"error": "user_id is required"}), 400

    # Save the graph visualization to a file
    plt.switch_backend('Agg')  # Use a non-interactive backend for Matplotlib
    recommender.visualize_graph(highlight_user=user_id)
    graph_filename = f"graph_{user_id}_{int(time.time())}.png"  # Add a timestamp
    graph_path = f"static/{graph_filename}"
    plt.savefig(graph_path)  # Save the graph as an image
    plt.close()

    return jsonify({"graph_url": f"/static/{graph_filename}"})

if __name__ == "__main__":
    app.run(debug=True)