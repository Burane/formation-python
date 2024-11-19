from sqlalchemy import Table, Column, Integer, String, MetaData, Float, create_engine
from sqlalchemy.exc import IntegrityError


class Database:
    
    def __init__(self) -> None:
        self.engine = create_engine("sqlite:///pokemon.db")
        self.conn = self.engine.connect()
        meta = MetaData()

        self.pokemons = Table(
            "pokemons", meta, 
            Column("id", Integer, primary_key = True), 
            Column("name", String, unique=True), 
            Column("height", Integer), 
            Column("weight", Integer), 
            Column("base_experience", Integer), 
            Column("types", String), 
            Column("bmi", Float), 
        )
        
        meta.create_all(self.engine)
        
        
    def save_pokemon(self, formated_data: dict) -> int:
        request = self.pokemons.insert().values(formated_data)
        try:
            self.conn.execute(request)
            self.conn.commit()
        except IntegrityError:
            return -1
        return 0
    
    def get_pokemons(self):
        request = self.pokemons.select()
        return self.conn.execute(request).fetchall()