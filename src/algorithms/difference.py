import pandas as pd
import logging


class Difference:

    def __init__(self):

        self.__periods = 1

    def __percentage_change(self, data: pd.DataFrame) -> pd.DataFrame:

        frame = data.ffill(axis=0, inplace=False)
        changes = 100 * frame.pct_change(periods=self.__periods, axis=0)
        logging.info(changes[self.__periods:])

        return changes[self.__periods:]

    def exc(self, data: pd.DataFrame) -> pd.DataFrame:
        """

        :param data: The index field is a datetime field
        :return:
        """

        return self.__percentage_change(data=data.copy())
