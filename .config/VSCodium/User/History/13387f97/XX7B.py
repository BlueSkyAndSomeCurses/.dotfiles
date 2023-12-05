import pandas as pd


def read_data():
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
    return df.head(1)

def summer_biggest(df):
    return df.loc[df["Gold"].idxmax()].ID


def difference_biggest(df):
    pass


def difference_biggest_relative(df):
    pass


def get_points(df):
    pass