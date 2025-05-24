"""Module menu.py"""
import logging
import os

import pandas as pd

import config
import src.functions.directories
import src.functions.objects


class Menu:
    """
    Menu
    """

    def __init__(self):
        """
        Constructor
        """

        self.__configurations = config.Config()

        self.__directories = src.functions.directories.Directories()
        self.__objects = src.functions.objects.Objects()

    def __contrasts(self, reference: pd.DataFrame):
        """

        :param reference:
        :return:
        """

        # Storage
        path = self.__configurations.menu_
        self.__directories.create(path=path)

        # Menu
        excerpt = reference.copy()[['catchment_id', 'catchment_name']].drop_duplicates()
        excerpt.sort_values(by='catchment_name', ascending=True, inplace=True)
        nodes = excerpt.to_dict(orient='records')

        return self.__objects.write(
            nodes=nodes, path=os.path.join(path, 'menu.json'))

    def exc(self, reference: pd.DataFrame):
        """

        :param reference: The reference sheet of the water level gauges.
        :return:
        """

        message = self.__contrasts(reference=reference)

        logging.info('Graphing Menu ->\n%s', message)
