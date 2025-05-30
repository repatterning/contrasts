"""Module interface.py"""
import logging

import numpy as np
import pandas as pd

import dask

import src.algorithms.data
import src.algorithms.difference
import src.algorithms.persist
import src.elements.partitions as pr


class Interface:
    """
    Interface
    """

    def __init__(self, listings: pd.DataFrame, reference: pd.DataFrame, arguments: dict):
        """

        :param listings: Includes a field of uniform resource identifiers for data acquisition, additionally
                         each instance includes a time series identification code
        :param reference: Each instance encodes a few gauge attributes/characteristics
        :param arguments: A set of arguments vis-à-vis calculation objectives.
        """

        self.__listings = listings
        self.__reference = reference
        self.__arguments = arguments

    @dask.delayed
    def __get_codes(self, catchment_id) -> pd.DataFrame:
        """

        :param catchment_id:
        :return:
        """

        return self.__listings.loc[
            self.__listings['catchment_id'] == catchment_id, ['ts_id', 'uri']]

    def exc(self, partitions: list[pr.Partitions]):
        """

        :param partitions: Refer to src/elements/partitions.py for more about Partitions
        :return:
        """

        catchment_id_ = np.array([partition.catchment_id for partition in partitions])
        catchment_id_ = np.unique(catchment_id_)

        # Tasks
        __get_data = dask.delayed(src.algorithms.data.Data().exc)
        __difference = dask.delayed(src.algorithms.difference.Difference().exc)
        __persist = dask.delayed(src.algorithms.persist.Persist(
            reference=self.__reference, frequency=self.__arguments.get('frequency')).exc)

        # Compute
        computations = []
        for catchment_id in catchment_id_:
            listing = self.__get_codes(catchment_id=catchment_id)
            data = __get_data(listing=listing)
            data = __difference(data=data)
            message = __persist(data=data, catchment_id=catchment_id)
            computations.append(message)
        messages = dask.compute(computations, scheduler='threads')[0]

        logging.info(messages)
