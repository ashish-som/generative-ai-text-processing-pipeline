"config loader"

import yaml
import os
from typing import Any, Dict
from interfaces.config_interface import ConfigInterface

class ConfigLoader(ConfigInterface):
    """
    A class to load and manage configuration from a YAML file.
    """
    def __init__(self, config_path: str):
        """
        Initializes the ConfigLoader with the path to the config file.

        Args:
            config_path (str): The path to the configuration file.
        """
        self.config_path = config_path
        self._config = self.load_config()

    def load_config(self) -> dict:
        """
        Loads the YAML configuration file from the specified path.
        """
        try:
            with open(self.config_path, 'r') as file:
                config = yaml.safe_load(file)
                if config is None:
                    return {}
                return config
        except FileNotFoundError:
            raise FileNotFoundError(f"Error: The configuration file was not found at {self.config_path}")
        except yaml.YAMLError as e:
            raise ValueError(f"Error parsing the YAML configuration file: {e}")

    def validate_config(self, schema: dict) -> bool:
        """
        Validates the configuration against a given schema.

        This is a simple validation. For more robust checks, a library like 'Cerberus' or 'JSON Schema' is recommended.
        """
        config = self.get_config()
        for key, expected_type in schema.items():
            if key not in config or not isinstance(config.get(key), expected_type):
                print(f"Validation failed: Key '{key}' is missing or has an incorrect type.")
                return False
        return True

    def get_config(self) -> dict:
        """
        Returns the loaded configuration dictionary.
        """
        return self._config

    def get_value(self, key: str, default: Any = None) -> Any:
        """
        Fetches a specific configuration value by key. Supports dot notation for nested keys.
        """
        keys = key.split('.')
        value = self._config
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value

    def get_input_paths(self) -> Dict[str, str]:
        """
        Fetches paths related to input files.
        """
        data_loader_config = self.get_value('data_loader', {})
        return {
            'file_path': data_loader_config.get('file_path'),
        }

    def get_output_path(self) -> str:
        """
        Fetches the output directory path.
        """
        return self.get_value('output.output_dir', '')

    def get_model_config(self) -> Dict[str, Any]:
        """
        Fetches the model configuration details.
        """
        return self.get_value('llm_model', {})

    def get_project_name(self) -> str:
        """
        Fetches the project name. This is not in your current config, so we'll provide a default.
        You can add 'project_name: "my_project"' to your config file to make this dynamic.
        """
        return self.get_value('project_name', 'generative-ai-text-processing-pipeline')
        
    def extract_from_pdf(self) -> bool:
        """
        Determines whether text should be extracted from PDFs based on the file extension.
        """
        file_path = self.get_value('data_loader.file_path', '')
        return file_path.lower().endswith('.pdf')
    
    def get_required_columns(self, is_pdf: bool = False) -> list:
        """
        Retrieves the list of required columns from the configuration based on file type.
        """
        if is_pdf:
            required_cols_str = self.get_value('data_loader.required_pdf_columns', '')
        else:
            required_cols_str = self.get_value('data_loader.required_tabular_columns', '')
            
        return [col.strip() for col in required_cols_str.split(',') if col.strip()]