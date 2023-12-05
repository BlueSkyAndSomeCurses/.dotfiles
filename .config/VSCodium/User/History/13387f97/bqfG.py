"""
Module to work with data
"""
import pandas as pd

def read_data():
    """
    Reads a csv file to create dataframe
    """
    df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)
    for col in df.columns:
        if col[:2] == '01':
            df.rename(columns={col: 'Gold'+col[4:]}, inplace=True)
        elif col[:2] == '02':
            df.rename(columns={col: 'Silver'+col[4:]}, inplace=True)
        elif col[:2] == '03':
            df.rename(columns={col: 'Bronze'+col[4:]}, inplace=True)
        elif col[:1] == '№':
            df.rename(columns={col: '#'+col[1:]}, inplace=True)

    names_ids = df.index.str.split('\\s\\(') # split the index by '('

    df.index = names_ids.str[0] # the [0] element is the country name (new index)
    df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

    df = df.drop('Totals')
    #print(df)

    return df

def first_country(df):
    """
    Returns first row of a data frame
    """
    return df.head(1)

def summer_biggest(df):
    """ 
    Returns a country which got the most gold medals in the summer
    """
    return df["Gold"].idxmax()

def difference_biggest(df):
    """ 
    returns a country which has the biggest difference
    between Gold medals in the summer and in the winter
    """
    return pd.Series.abs(df["Gold"] - df["Gold.1"]).idxmax()

def difference_biggest_relative(df):
    """ 
    returns biggest relationg of difference of gold medals in summer and winter to total amount of medals
    """
    tmp_df = df.loc[(df["Gold"] > 0)&(df["Gold.1"]>0)].loc[:, ["Gold", "Gold.1", "Gold.2", "ID"]] 

    return pd.Series.abs((tmp_df["Gold"]-tmp_df["Gold.1"])/tmp_df["Gold.2"]).idxmax()

def get_points(df):
    """
    creates a column points, and returns its series
    """
    df["Points"] = df["Gold.2"] * 3 + df["Silver.2"] * 2 + df["Bronze.2"] 
    return df["Points"]
