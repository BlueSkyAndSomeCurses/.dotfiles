"""
Module to work with data
"""
import pandas as pd

def read_data():
    """
    Reads a csv file to create dataframe
    """
    data_f = pd.read_csv('olympics.csv', index_col=0, skiprows=1)
    for col in data_f.columns:
        if col[:2] == '01':
            data_f.rename(columns={col: 'Gold'+col[4:]}, inplace=True)
        elif col[:2] == '02':
            data_f.rename(columns={col: 'Silver'+col[4:]}, inplace=True)
        elif col[:2] == '03':
            data_f.rename(columns={col: 'Bronze'+col[4:]}, inplace=True)
        elif col[:1] == '№':
            data_f.rename(columns={col: '#'+col[1:]}, inplace=True)

    names_ids = data_f.index.str.split('\\s\\(') # split the index by '('

    data_f.index = names_ids.str[0] # the [0] element is the country name (new index)
    data_f['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or 
                                            #ID (take first 3 characters from that)

    data_f = data_f.drop('Totals')
    #print(data_f)

    return data_f

def first_country(data_f):
    """
    Returns first row of a data frame
    """
    return data_f.head(1)

def summer_biggest(data_f):
    """ 
    Returns a country which got the most gold medals in the summer
    """
    return data_f["Gold"].idxmax()

def difference_biggest(data_f):
    """ 
    returns a country which has the biggest difference
    between Gold medals in the summer and in the winter
    """
    return pd.Series.abs(data_f["Gold"] - data_f["Gold.1"]).idxmax()

def difference_biggest_relative(data_f):
    """ 
    returns biggest relationg of difference of gold medals
    in summer and winter to total amount of medals
    """
    tmp_data_f = data_f.loc[(data_f["Gold"] > 0)&(data_f["Gold.1"]>0)].loc[:, \
    ["Gold", "Gold.1", "Gold.2", "ID"]]

    return pd.Series.abs((tmp_data_f["Gold"]-tmp_data_f["Gold.1"])/tmp_data_f["Gold.2"]).idxmax()

def get_points(data_f):
    """
    creates a column points, and returns its series
    """
    data_f["Points"] = data_f["Gold.2"] * 3 + data_f["Silver.2"] * 2 + data_f["Bronze.2"]
    return data_f["Points"]
