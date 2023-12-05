import pandas as pd


def read_data(path_to_file: str) -> pd.DataFrame:
    """
    reads a file and converts it to data frame
    """

    return pd.read_csv(path_to_file)


def max_counties(df):
    """
    returns a name of a state with the biggest amount of countries
    """
    return df.groupby("STNAME").CTYNAME.count().idxmax()


def max_difference(df):
    pass


def conditional_counties(df):
    pass


if __name__ == "__main__":
    print(read_data("census.csv"))
