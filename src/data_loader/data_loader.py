import pandas as pd
import fitz
import os
from interfaces.data_loader_interface import DataLoaderInterface

"""
Module: data_loader.py
Purpose: Implements the functionality for loading datasets and validating required columns.

Classes:
    DataLoader: Handles dataset loading and ensures the presence of required columns.

Usage:
    This module is responsible for reading datasets (e.g., from CSV files, excel files or pdfs) and
    validating that the necessary columns exist in the data. It adheres to the
    DataLoaderInterface to maintain consistency.
"""


class TabularDataLoader(DataLoaderInterface):
    """
    This class   loads data from both Excel (.xlsx) and CSV (.csv) files.
    """
    def __init__(self, file_path: str):
        self.file_path = file_path
        self._data = None
        self.file_type = self._get_file_type()

    def _get_file_type(self) -> str:
        """Determines the file type based on the file extension."""
        if self.file_path.lower().endswith('.csv'):
            return 'csv'
        elif self.file_path.lower().endswith(('.xls', '.xlsx')):
            return 'excel'
        else:
            return 'unknown'

    def load_data(self) -> pd.DataFrame:
        """Loads the dataset from the specified file based on its type."""
        try:
            if self.file_type == 'csv':
                self._data = pd.read_csv(self.file_path)
            elif self.file_type == 'excel':
                self._data = pd.read_excel(self.file_path)
            else:
                raise ValueError("Unsupported file format.")
            print(f"Successfully loaded data from {self.file_path}")
            return self._data
        except FileNotFoundError:
            print(f"Error: The file {self.file_path} was not found.")
            return pd.DataFrame()
        except ValueError as ve:
            print(f"File loading error: {ve}")
            return pd.DataFrame()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return pd.DataFrame()

    def validate_columns(self, required_columns: list[str]) -> bool:
        if self._data is None or self._data.empty:
            print("No data loaded to validate.")
            return False
        missing_columns = [col for col in required_columns if col not in self._data.columns]
        if missing_columns:
            print(f"Validation failed. Missing columns: {', '.join(missing_columns)}")
            return False
        print("All required columns are present.")
        return True

    def get_data(self) -> pd.DataFrame:
        if self._data is None:
            print("Data has not been loaded yet. Please call load_data() first.")
        return self._data if self._data is not None else pd.DataFrame()


class PDFDataLoader(DataLoaderInterface):
    """
    A concrete implementation for loading data from a PDF file.
    """
    def __init__(self, file_path: str):
        self.file_path = file_path
        self._data = None

    def load_data(self) -> pd.DataFrame:
        try:
            doc = fitz.open(self.file_path)
            text_content = "".join([page.get_text() for page in doc])
            doc.close()
            file_name = os.path.basename(self.file_path)
            map_id, _ = os.path.splitext(file_name)
            self._data = pd.DataFrame([{'map_id': map_id, 'text': text_content}])
            print(f"Successfully loaded data from {self.file_path}")
            return self._data
        except FileNotFoundError:
            print(f"Error: The file {self.file_path} was not found.")
            return pd.DataFrame()
        except Exception as e:
            print(f"An error occurred while loading the PDF file: {e}")
            return pd.DataFrame()

    def validate_columns(self, required_columns: list[str]) -> bool:
        if self._data is None or self._data.empty:
            print("No data loaded to validate.")
            return False
        missing_columns = [col for col in required_columns if col not in self._data.columns]
        if missing_columns:
            print(f"Validation failed. Missing columns: {', '.join(missing_columns)}")
            return False
        print("All required columns are present.")
        return True

    def get_data(self) -> pd.DataFrame:
        if self._data is None:
            print("Data has not been loaded yet. Please call load_data() first.")
        return self._data if self._data is not None else pd.DataFrame()


class DataLoader(DataLoaderInterface):
    """
    Handles dataset loading for various file types (CSV, XLSX, PDF) and
    validates the presence of required columns.
    """
    def __init__(self, file_path: str):
        self.file_path = file_path
        self._loader = self._get_appropriate_loader()
        
    def _get_appropriate_loader(self):
        """Returns the correct loader instance based on the file extension."""
        if self.file_path.lower().endswith(('.csv', '.xls', '.xlsx')):
            return TabularDataLoader(self.file_path)
        elif self.file_path.lower().endswith('.pdf'):
            return PDFDataLoader(self.file_path)
        else:
            raise ValueError("Unsupported file format. Please provide a .csv, .xlsx, or .pdf file.")

    def load_data(self) -> pd.DataFrame:
        """Loads data using the selected loader."""
        return self._loader.load_data()

    def validate_columns(self, required_columns: list[str]) -> bool:
        """Validates columns using the selected loader."""
        return self._loader.validate_columns(required_columns)

    def get_data(self) -> pd.DataFrame:
        """Returns the data from the selected loader."""
        return self._loader.get_data()