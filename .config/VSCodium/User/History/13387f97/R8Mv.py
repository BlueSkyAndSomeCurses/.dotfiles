"""
Module to work with data
"""
import pandas as pd

def read_data():
    """
    Reads a csv file to create dataframe
    """
    data_frame = pd.read_csv('olympics.csv', index_col=0, skiprows=1)
    for col in data_frame.columns:
        if col[:2] == '01':
            data_frame.rename(columns={col: 'Gold'+col[4:]}, inplace=True)
        elif col[:2] == '02':
            data_frame.rename(columns={col: 'Silver'+col[4:]}, inplace=True)
        elif col[:2] == '03':
            data_frame.rename(columns={col: 'Bronze'+col[4:]}, inplace=True)
        elif col[:1] == '№':
            data_frame.rename(columns={col: '#'+col[1:]}, inplace=True)

    names_ids = data_frame.index.str.split('\\s\\(') # split the index by '('

    data_frame.index = names_ids.str[0] # the [0] element is the country name (new index)
    data_frame['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

    data_frame = data_frame.drop('Totals')
    #print(data_frame)

    return data_frame

def first_country(data_frame):
    """
    Returns first row of a data frame
    """
    return data_frame.head(1)

def summer_biggest(data_frame):
    """ 
    Returns a country which got the most gold medals in the summer
    """
    return data_frame["Gold"].idxmax()

def difference_biggest(data_frame):
    """ 
    returns a country which has the biggest difference
    between Gold medals in the summer and in the winter
    """
    return pd.Series.abs(data_frame["Gold"] - data_frame["Gold.1"]).idxmax()

def difference_biggest_relative(data_frame):
    """ 
    returns biggest relationg of difference of gold medals in summer and winter to total amount of medals
    """
    tmp_data_frame = data_frame.loc[(data_frame["Gold"] > 0)&(data_frame["Gold.1"]>0)].loc[:, ["Gold", "Gold.1", "Gold.2", "ID"]] 

    return pd.Series.abs((tmp_data_frame["Gold"]-tmp_data_frame["Gold.1"])/tmp_data_frame["Gold.2"]).idxmax()

def get_points(data_frame):
    """
    creates a column points, and returns its series
    """
    data_frame["Points"] = data_frame["Gold.2"] * 3 + data_frame["Silver.2"] * 2 + data_frame["Bronze.2"] 
    return data_frame["Points"]
