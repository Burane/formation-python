import pandas as pd
from sqlalchemy import create_engine

try:
    # Connect to the SQLite database
    engine = create_engine("sqlite:///pokemon.db")
except:
    print('Error ; db file not found.')

try:
    # Load the pokemon table into a pandas DataFrame
    df = pd.read_sql("SELECT * FROM pokemon", engine)
except:
    print("Error ; empty db table.")
    exit(0)

# Display the first few rows of data
print("First few rows of the dataset:")
print(df.head())