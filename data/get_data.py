import pandas as pd
import urllib.request


def get_data(url):
    # Simulate a web browser request.
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    # Read the data into data frame
    df = pd.read_csv(urllib.request.urlopen(req), sep=',')
    return df
