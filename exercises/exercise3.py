import pandas as pd
import sqlalchemy

DATA_URL = 'https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv'
COLUMNS_TO_KEEP_NUMBERS = [0, 1, 2, 12, 22, 32, 42, 52, 62, 72]
NAME_LIST = ["date", "CIN", "name", "petrol", "diesel",
             "gas", "electro", "hybrid", "plugInHybrid", "others"]


def data_extraction(data_url, column_numbers, rename_list):
    '''
    Extract data from the url.
    Ignore the first 6 lines and last 4 lines as metadata.
    Keep only needed columns.
                Rename them.
    '''
    df = pd.read_csv(data_url, skiprows=6, skipfooter=4,
                     encoding='latin1', engine='python', sep=';')
    df = df.iloc[:, column_numbers]
    df.columns = rename_list
    return df


def data_validation(data):
    # Validate date column as string
    data = data[data["date"].astype(str).apply(lambda x: isinstance(x, str))]
    # Validate name column as string
    data = data[data["name"].astype(str).apply(lambda x: isinstance(x, str))]
    # Validate CINs
    data = data[data["CIN"].astype(str).apply(
        lambda x: isinstance(x, str) and len(x) == 5 and x.isdigit())]

    # Validate other columns as positive integers
    numeric_columns = ["petrol", "diesel", "gas",
                       "electro", "hybrid", "plugInHybrid", "others"]
    for column in numeric_columns:
        # Convert column to numeric type, invalid values become NaN
        data[column] = pd.to_numeric(data[column], errors='coerce')
        # Filter rows with positive integers
        data = data[data[column].fillna(-1).ge(0)]

    # Drop rows with any invalid values
    data = data.dropna()
    return data


def data_write(data):
    # Create the SQLAlchemy engine
    engine = sqlalchemy.create_engine("sqlite:///cars.sqlite")

    # Write the DataFrame to the SQLite database
    data.to_sql("cars", engine, if_exists="replace", index=False,
                dtype={
                    "date": sqlalchemy.TEXT,
                    "name": sqlalchemy.TEXT,
                    "CIN": sqlalchemy.TEXT,
                    'petrol': sqlalchemy.BIGINT,
                    'diesel': sqlalchemy.BIGINT,
                    'gas': sqlalchemy.BIGINT,
                    'electro': sqlalchemy.BIGINT,
                    'hybrid': sqlalchemy.BIGINT,
                    'plugInHybrid': sqlalchemy.BIGINT,
                    'others': sqlalchemy.BIGINT})


def main():
    data = data_extraction(DATA_URL, COLUMNS_TO_KEEP_NUMBERS, NAME_LIST)
    data = data_validation(data)
    data_write(data)


if __name__ == '__main__':
    main()
