class DataCleaning():
    
    @staticmethod
    def clean_data(data: dict) -> dict:
        
        id: int = data["id"]
        name: str = data["name"]
        height: float = data["height"]
        weight: float = data["weight"]
        base_experience: int = data["base_experience"]
        types: list[str] = []
        
        for type in data["types"]:
            types.append(type["type"]["name"])
            
        types_str: str = ", ".join(types)
        
        pokemon_data: dict = {
            "id": id,
            "name": name,
            "height": height,
            "weight": weight,
            "base_experience": base_experience,
            "types": types_str,
        }
        
        return pokemon_data
        