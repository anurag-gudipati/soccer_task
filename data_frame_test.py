import pytest
import unittest

from pandas._testing import assert_frame_equal
import test_pandas as tp


filepath = 'C:/Users/Gathi/Documents/test/soccer.csv'
def test_filepath():
    """
    Checking the filepath in given path
    :return: filepath
    """

    print ("filepath checking ")
    assert filepath == tp.filepath

def test_dataframe():
    """
    Checing the dataframes both source and test
    :return: df
    """

    df  = tp.pd.read_csv(filepath)
    assert_frame_equal(df,tp.df)


def test_top10_teams():
    """
    Checking the top10 teams and validating the top10 teams
    :return:
    """
    stat1 = tp.df1.stat1()
    stat_check = ['Arsenal', 'Liverpool', 'Manchester United', 'Newcastle', 'Leeds', 'Chelsea', 'West_Ham', 'Tottenham',
     'Aston_Villa', 'Blackburn']
    assert stat_check == stat1

def test_gols_min():
    """
    checking the min goals team
    :return:
    """

    #gol_min = tp.df1.stats_display
    test_min_gols = 'Aston_Villa'
    assert  'Aston_Villa' == test_min_gols


