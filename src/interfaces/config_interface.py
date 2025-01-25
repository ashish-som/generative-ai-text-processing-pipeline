"""
Module: config_interface.py
Purpose: Defines the interface for the configuration loader. This ensures all 
         configuration loaders adhere to a standard structure.

Classes:
    ConfigInterface: Abstract base class for configuration loaders.
"""

from abc import ABC, abstractmethod
from typing import Any


class ConfigInterface(ABC):
    """
    Abstract base class for configuration loaders.
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
