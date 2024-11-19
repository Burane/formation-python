from flask import Flask, request, jsonify
from pipeline import Pipeline

app = Flask(__name__)
pipeline = Pipeline()

@app.route('/process_pokemon', methods=['POST'])
def process_pokemon():
    pokemon_name = request.json.get('name')

    if not pokemon_name:
        return jsonify({"error": "Please provide a Pokemon name"}), 400

    result = pipeline.process_pokemon(pokemon_name)

    if result == 'success':
        return jsonify({"message": f"Processing of {pokemon_name} complete."}), 200
    else:
        return jsonify({"error": result}), 400

if __name__ == '__main__':
    app.run(debug=True)