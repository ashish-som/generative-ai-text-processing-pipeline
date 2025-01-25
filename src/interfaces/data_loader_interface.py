"""
Module: data_loader_interface.py
Purpose: Defines the interface for data loader. This ensures data loader
         adheres to a standard structure for loading and validating required columns.

Classes:
    DataLoaderInterface: Abstract base class for data loader.
"""

from abc import ABC, abstractmethod
import pandas as pd


class DataLoaderInterface(ABC):
    """
    Abstract base class for data loader.
    """

    @abstractmethod
    def load_data(self) -> pd.DataFrame:
        """
        Loads the dataset.

        Returns:
            pd.DataFrame: The loaded dataset.
        """
        pass

    @abstractmethod
    def validate_columns(self, required_columns: list[str]) -> bool:
        """
        Validates that the required columns are present in the dataset.

        Args:
            required_columns (list[str]): A list of required column names.

        Returns:
            bool: True if all required columns are present, False otherwise.
        """
        pass

    @abstractmethod
    def get_data(self) -> pd.DataFrame:
        """
        Returns the loaded dataset.

        Returns:
            pd.DataFrame: The dataset.
        """
        pass
