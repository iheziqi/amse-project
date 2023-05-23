import pandas as pd
from sqlalchemy import create_engine, Integer, Text, Float

URL = 'https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv'

# Get the csv file from website
df = pd.read_csv(URL, delimiter=';', encoding='utf-8')

# Define SQLite types for columns
column_types = {
    "column_1": Integer,
    "column_2": Text,
    "column_3": Text,
    "column_4": Text,
    "column_5": Text,
    "column_6": Text,
    "column_7": Float,
    "column_8": Float,
    "column_9": Integer,
    "column_10": Float,
    "column_11": Text,
    "column_12": Text,
    "geo_punkt": Text

}
# Create a SQLAlchemy engine to connect to the SQLite database
engine = create_engine('sqlite:///airports.db')

# Convert the DataFrame to a SQL table using the engine
df.to_sql('your_table_name', engine, if_exists='replace',
          index=False, dtype=column_types)

# Close the database connection
engine.dispose()
