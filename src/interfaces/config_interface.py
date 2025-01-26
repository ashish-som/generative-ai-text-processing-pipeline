"""
Module: config_interface.py
Purpose: Defines the interface for the configuration loader. This ensures all 
         configuration loaders adhere to a standard structure.

Classes:
    ConfigInterface: Abstract base class for configuration loaders.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict


class ConfigInterface(ABC):
    """
    Abstract base class for configuration loaders, tailored to handle the specific fields
    defined in the 'config.yaml' file for the LLM-based project.
    """

    @abstractmethod
    def load_config(self) -> dict:
        """
        Loads the configuration file.

        Returns:
            dict: A dictionary containing the configuration settings.
        """
        pass

    @abstractmethod
    def validate_config(self, schema: dict) -> bool:
        """
        Validates the configuration against a given schema.

        Args:
            schema (dict): A dictionary defining the expected schema.

        Returns:
            bool: True if the configuration is valid, False otherwise.
        """
        pass

    @abstractmethod
    def get_config(self) -> dict:
        """
        Returns the loaded configuration.

        Returns:
            dict: The configuration settings.
        """
        pass

    @abstractmethod
    def get_value(self, key: str, default: Any = None) -> Any:
        """
        Fetches a specific configuration value by key.

        Args:
            key (str): The key for the configuration setting.
            default (Any, optional): Default value if the key is not found. Defaults to None.

        Returns:
            Any: The configuration value.
        """
        pass

    @abstractmethod
    def get_input_paths(self) -> Dict[str, str]:
        """
        Fetches paths related to input files (e.g., Excel, PDF).

        Returns:
            dict: Dictionary containing 'excel_path', 'pdf_path', and other relevant input paths.
        """
        pass

    @abstractmethod
    def get_output_path(self) -> str:
        """
        Fetches the output directory path.

        Returns:
            str: The path to the output directory.
        """
        pass

    @abstractmethod
    def get_model_config(self) -> Dict[str, Any]:
        """
        Fetches the model configuration details such as model name and temperature.

        Returns:
            dict: Dictionary containing model configuration (e.g., 'model_name', 'temperature').
        """
        pass

    @abstractmethod
    def get_project_name(self) -> str:
        """
        Fetches the project name.

        Returns:
            str: The project name.
        """
        pass

    @abstractmethod
    def extract_from_pdf(self) -> bool:
        """
        Determines whether text should be extracted from PDFs.

        Returns:
            bool: True if extraction from PDFs is enabled, False otherwise.
        """
        pass