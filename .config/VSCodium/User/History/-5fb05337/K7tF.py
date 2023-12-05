import pandas as pd


def read_data(path_to_file: str) -> pd.DataFrame:
    """
    reads a file and converts it to data frame
    """

    return pd.read_csv(path_to_file)


def max_counties(data_f: pd.DataFrame) -> str:
    """
    returns a name of a state with the biggest amount of countries
    """
    return data_f.groupby("STNAME").CTYNAME.count().idxmax()


def max_difference(data_f):
    pass


def conditional_counties(data_f):
    pass


if __name__ == "__main__":
    print(read_data("census.csv"))
