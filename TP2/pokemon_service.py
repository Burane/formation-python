import requests

class PokemonService:
    API_BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

    @staticmethod
    def get_pokemon_data(pokemon_name) -> dict:
        response = requests.get(f"{PokemonService.API_BASE_URL}{pokemon_name.lower()}")
        if response.status_code == 200:
            return response.json()  # Retourne les données JSON
        else:
            print(f"Pokemon {pokemon_name} not found.")
            return None
 