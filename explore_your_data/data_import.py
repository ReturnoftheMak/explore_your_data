# Take in the basic version of the Netflix output and convert to dataframe
# This is mainly for testing, we'll need to work out a different method to import data from a web interface

# %% Package Imports

import pandas as pd


# %% Example filepath

filepath = r'C:\Users\Mak\Documents\Python Scripts\explore_your_data\data\NetflixViewingHistory_test1.csv'

# %% Create dataframe from csv

def data_import(file):
    """Takes a csv file as exported from Netflix and returns a dataframe

    Args:
        file (str): filepath
    
    Returns:
        pandas.core.frame.DataFrame
    """

    df = pd.read_csv(file)

    # The Title col contains 3 parts: Show, Season, EpisodeName

    df_split = df.Title.str.split(":",expand=True)

    df['Show'] = df_split[0]
    df['Season'] = df_split[1]

    # The Episode name contains semicolons, because life is never that easy

    df['EpisodeName'] = df_split[2] + df_split[3].fillna('') + df_split[4].fillna('')

    df = df[['Show', 'Season', 'EpisodeName', 'Date']]

    return df
