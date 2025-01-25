"""
Module: data_loader.py
Purpose: Implements the functionality for loading datasets and validating required columns.

Classes:
    DataLoader: Handles dataset loading and ensures the presence of required columns.

Usage:
    This module is responsible for reading datasets (e.g., from CSV files, excel files or pdfs) and 
    validating that the necessary columns exist in the data. It adheres to the 
    DataLoaderInterface to maintain consistency.

Example:
    from data_loader import DataLoader

    loader = DataLoader(filepath="data.csv")
    data = loader.load_data()
    if loader.validate_columns(["column1", "column2"]):
        print("Data is valid.")
    else:
        print("Missing required columns.")
"""