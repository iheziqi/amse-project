import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_germany_county_list():
    # Specify the URL of the Wikipedia page containing the table
    url = 'https://de.wikipedia.org/wiki/Liste_der_Landkreise_in_Deutschland'

    # Send a GET request to the URL and retrieve the page content
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'lxml')

    # Find the table element on the page
    table = soup.find('table', class_='wikitable')

    # Convert the table to a DataFrame
    if table:
        table_data = []
        headers = []
        rows = table.find_all('tr')
        for i, row in enumerate(rows):
            cells = row.find_all(['th', 'td'])
            if i == 0:
                # Exclude the last column header
                headers = [cell.get_text(strip=True) for cell in cells[:-1]]
            else:
                # Exclude the last column data
                table_data.append([cell.get_text(strip=True)
                                  for cell in cells[:-1]])

        df = pd.DataFrame(table_data, columns=headers)
        return df
    else:
        print(f"No table found on the Wikipedia page: {url}")
        return


def get_age_group():
    # Define the mapping rules
    mapping = {
        1: '0-20yrs',
        2: '20-50yrs',
        3: '50-65yrs',
        4: '65-80yrs',
        5: 'above 80yrs'
    }

    # Create a DataFrame with the values and detail information
    data = {
        'Value': list(range(1, 6)),
        'Detail': [mapping[value] for value in range(1, 6)]
    }

    df = pd.DataFrame(data)

    return df


def get_activity_dest():
  # Define the mapping rules
    mapping = {
        1: '1: Work place',
        2: '2: Education',
        3: '3: Shopping',
        4: '4: Leisure/free-time',
        5: '5: Personal matters',
        6: '6: Other',
        7: '7: Home'
    }

    # Create a DataFrame with the values and detail information
    data = {
        'Value': list(range(1, 8)),
        'Activity': [mapping[value] for value in range(1, 8)]
    }

    df = pd.DataFrame(data)

    return df
