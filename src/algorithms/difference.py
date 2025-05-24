"""Module difference.py"""
import logging

import pandas as pd


class Difference:
    """
    Calculates percentage difference between sequential measures, per gauge time series.
    """

    def __init__(self):
        """
        Constructor
        """

        self.__periods = 1

    def __percentage_change(self, data: pd.DataFrame) -> pd.DataFrame:
        """

        :param data: Each field represents a distinct gauge.
        :return:
        """

        frame = data.ffill(axis=0, inplace=False)
        changes = 100 * frame.pct_change(periods=self.__periods, axis=0)
        logging.info(changes[self.__periods:])

        return changes[self.__periods:]

    def exc(self, data: pd.DataFrame) -> pd.DataFrame:
        """

        :param data: The index field is a datetime field.  Each field represents a distinct gauge.
        :return:
        """

        return self.__percentage_change(data=data.copy())
