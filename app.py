from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Game state
game_data = {
    "colors": ["red", "green", "blue", "yellow", "purple", "orange"],
    "target_color": None,
    "guesses": []
}

# Start a new game
@app.route('/start', methods=['POST'])
def start_game():
    game_data["target_color"] = random.choice(game_data["colors"])
    game_data["guesses"] = []
    return jsonify({"message": "New game started! Guess a color."})

# Make a guess
@app.route('/guess', methods=['POST'])
def guess_color():
    data = request.get_json()
    guess = data.get("color", "").lower()

    if guess not in game_data["colors"]:
        return jsonify({"error": "Invalid color. Try again."}), 400

    game_data["guesses"].append(guess)
    result = "correct" if guess == game_data["target_color"] else "incorrect"
    return jsonify({"your_guess": guess, "result": result})

# Check game status
@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({
        "total_guesses": len(game_data["guesses"]),
        "last_guess": game_data["guesses"][-1] if game_data["guesses"] else None
    })

# Get all guess history
@app.route('/history', methods=['GET'])
def get_history():
    return jsonify({"guesses": game_data["guesses"]})

# Reset the game
@app.route('/reset', methods=['POST'])
def reset_game():
    game_data["target_color"] = None
    game_data["guesses"] = []
    return jsonify({"message": "Game reset. Start a new game."})

if __name__ == "__main__":
    app.run(debug=True)
