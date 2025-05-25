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
