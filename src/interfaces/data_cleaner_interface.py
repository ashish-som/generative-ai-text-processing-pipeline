"""
Module: data_cleaner_interface.py
Purpose: Defines the interface for data cleaning.

Classes:
    DataCleanerInterface: Abstract base class for cleaning data.
"""

from abc import ABC, abstractmethod
import pandas as pd


class DataCleanerInterface(ABC):
    """
    Abstract base class for data cleaning.
    """

    @abstractmethod
    def clean_data(self, data: pd.DataFrame, text_columns: list[str]) -> pd.DataFrame:
        """
        Orchestrates all data cleaning steps.

        Args:
            data (pd.DataFrame): The input DataFrame.
            text_columns (list[str]): List of columns to clean.

        Returns:
            pd.DataFrame: The cleaned DataFrame.
        """
        pass

    @abstractmethod
    def replace_missing_values(self, data: pd.DataFrame, text_columns: list[str]) -> pd.DataFrame:
        """
        Replaces missing values in the specified text columns with an empty string ('').

        Args:
            data (pd.DataFrame): The input DataFrame.
            text_columns (list[str]): List of columns to clean.

        Returns:
            pd.DataFrame: The DataFrame with missing values replaced.
        """
        pass

    @abstractmethod
    def remove_duplicates(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Removes duplicate rows from the DataFrame.

        Args:
            data (pd.DataFrame): The input DataFrame.

        Returns:
            pd.DataFrame: The DataFrame with duplicates removed.
        """
        pass

    @abstractmethod
    def remove_non_ascii_characters(self, data: pd.DataFrame, text_columns: list[str]) -> pd.DataFrame:
        """
        Removes non-ASCII characters from the specified text columns.

        Args:
            data (pd.DataFrame): The input DataFrame.
            text_columns (list[str]): List of columns to clean.

        Returns:
            pd.DataFrame: The DataFrame with non-ASCII characters removed.
        """
        pass
