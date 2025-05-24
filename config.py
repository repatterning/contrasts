"""
Module config
"""
import os
import datetime


class Config:
    """
    Class Config

    For project settings
    """

    def __init__(self):
        """
        Constructor
        """

        self.warehouse: str = os.path.join(os.getcwd(), 'warehouse')
        self.contrasts_ = os.path.join(self.warehouse, 'contrasts')
        self.points_ = os.path.join(self.contrasts_, 'points')
        self.menu_ = os.path.join(self.contrasts_, 'menu')

        # Template
        self.s3_parameters_key = 's3_parameters.yaml'
        self.arguments_key = 'contrasts/arguments.json'
        self.metadata_ = 'contrasts/external'

        # The prefix of the Amazon repository where the quantiles will be stored
        self.prefix = 'warehouse/contrasts'

        # Times
        starting = datetime.datetime.strptime('2024-02-29 00:00:00', '%Y-%m-%d %H:%M:%S')
        ending = datetime.datetime.strptime('2024-03-01 00:00:00', '%Y-%m-%d %H:%M:%S')
        timespan = ending - starting
        timespan.total_seconds()

        self.shift = int(1000 * timespan.total_seconds())

        self.leap = '2024-01-01'
