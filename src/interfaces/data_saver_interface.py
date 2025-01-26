"""
Module: data_saver_interface.py
Purpose: Defines the interface for saving data.

Classes:
    DataSaverInterface: Abstract base class for saving data to a file.
"""

from abc import ABC, abstractmethod
import pandas as pd


class DataSaverInterface(ABC):
    """
    Abstract base class for saving data to a file.
    """

    @abstractmethod
    def save_to_csv(self, data: pd.DataFrame, file_path: str) -> None:
        """
        Saves the DataFrame to a CSV file.

        Args:
            data (pd.DataFrame): The DataFrame to save.
            file_path (str): The path of the file where data should be saved.
        """
        pass
