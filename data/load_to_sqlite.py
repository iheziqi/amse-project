import sqlite3
import os


def load_to_database(df, table_name):
    # Connect to the SQLite database or create a new one if it doesn't exist
    db_file = 'data.sqlite'
    if not os.path.exists(db_file):
        # Create an empty database file
        open(db_file, 'w').close()

  # Connect to the SQLite database
    conn = sqlite3.connect(database=db_file)

    # Write the DataFrame to a SQLite table
    df.to_sql(table_name, conn, if_exists='replace', index=False)

    # Close the database connection
    conn.close()
