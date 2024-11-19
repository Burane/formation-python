from flask import Flask, jsonify, request
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

@app.route('/process_pokemon', methods=['POST'])
def process_pokemon():
    pokemon_name = request.json.get('name')
    print("pokemon_name",pokemon_name)
    
    data = fetch_pokemon(pokemon_name)
    print("data",data)
    if data is None:
        return jsonify({"message": f"Pokemon {pokemon_name} not found."}), 404
    
    parsed_data = parse_data(data)
    
    try:
        save_pokemon(parsed_data)
    except IntegrityError:
        return jsonify({"error": f"Pokemon {pokemon_name} already stored in DB."}), 409
        
    return jsonify({"message": f"Processing of {pokemon_name} complete."}), 200
    
    
def parse_data(data: dict) -> dict:
        return {
            "id": data["id"],
            "name": data["name"],
            "height": data["height"],
            "weight": data["weight"],
            "base_experience": data["base_experience"],
            "types": ", ".join([type["type"]["name"] for type in data["types"]]),
            "bmi": calc_bmi(data["weight"], data["height"])
        }
        
def calc_bmi(weight: float, height: float) -> float:
    return weight / (height ** 2)

def fetch_pokemon(pokemon_name: str) -> dict | None:
    import requests
    
    API_BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
    response = requests.get(f"{API_BASE_URL}{pokemon_name.lower()}")
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Pokemon {pokemon_name} not found.")
        return None

def save_pokemon(pokemon: dict) -> None:
    from sqlalchemy import Table, Column, Integer, String, MetaData, Float, create_engine

    engine = create_engine("sqlite:///pokemon.db")
    meta = MetaData()

    pokemons = Table(
        "pokemon", meta, 
        Column("id", Integer, primary_key = True), 
        Column("name", String, unique=True), 
        Column("height", Integer), 
        Column("weight", Integer), 
        Column("base_experience", Integer), 
        Column("types", String), 
        Column("bmi", Float), 
    )
    
    meta.create_all(engine)
    
    with engine.connect() as conn:
        request = pokemons.insert().values(pokemon)
        conn.execute(request)
        conn.commit()
        
        
if __name__ == '__main__':
    app.run(debug=True)