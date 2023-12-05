"""
Module to work with data
"""
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


def max_difference(data_f: pd.DataFrame) -> str:
    """
    returns a name of a country with the biggest change of population
    """

    tmp_f = df.loc[df["COUNTY"] != 0]
    max_people = tmp_f.loc[
        :,
        [
            "POPESTIMATE2010",
            "POPESTIMATE2011",
            "POPESTIMATE2012",
            "POPESTIMATE2013",
            "POPESTIMATE2014",
            "POPESTIMATE2015",
        ],
    ].max(axis="columns")

    min_people = tmp_f.loc[
        :,
        [
            "POPESTIMATE2010",
            "POPESTIMATE2011",
            "POPESTIMATE2012",
            "POPESTIMATE2013",
            "POPESTIMATE2014",
            "POPESTIMATE2015",
        ],
    ].min(axis="columns")

    return tmp_f.loc[pd.Series.abs(max_people - min_people).idxmax()].CTYNAME


def conditional_counties(data_f: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a data frame with state name and county name,
    if county contains Washinton, and popluation2015 greater that popuation 2014
    """
    tmp_f = data_f[data_f["REGION"].isin([1, 2])]
    tmp_f = tmp_f.loc[
        (tmp_f["CTYNAME"].str.contains("Washington"))
        & (tmp_f["POPESTIMATE2015"] > tmp_f["POPESTIMATE2014"])
    ]
    return tmp_f.loc[:, ["STNAME", "CTYNAME"]]


if __name__ == "__main__":
    print(read_data("census.csv"))
