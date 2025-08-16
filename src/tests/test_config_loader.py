import pytest
import os
import yaml
from src.config_loader.config_loader import ConfigLoader

# Define a fixture to create a temporary, mock config.yaml file for testing
@pytest.fixture
def mock_config_file(tmp_path):
    config_data = {
        "data_loader": {
            "file_path": "data/input/sample.xlsx",
            "required_tabular_columns": "id,title,abstract",
            "required_pdf_columns": "map_id,text"
        },
        "llm_model": {
            "provider": "openai",
            "model_name": "o4-mini-2025-04-16",
            "api_key_name": "OPENAI_API_KEY",
            "temperature": 0.7
        },
        "output": {
            "output_dir": "data/output",
            "output_csv_file": "results.csv",
            "output_excel_file": "results.xlsx"
        }
    }
    file_path = tmp_path / "config.yaml"
    with open(file_path, "w") as f:
        yaml.dump(config_data, f)
    return str(file_path)

def test_config_loader_initialization_and_loading(mock_config_file):
    """
    Test if the ConfigLoader can be initialized and loads the config data correctly.
    """
    loader = ConfigLoader(mock_config_file)
    config = loader.get_config()
    assert isinstance(config, dict)
    assert config['data_loader']['file_path'] == "data/input/sample.xlsx"
    assert config['llm_model']['provider'] == "openai"

def test_get_value(mock_config_file):
    """
    Test the get_value method for nested keys and default values.
    """
    loader = ConfigLoader(mock_config_file)
    assert loader.get_value("llm_model.model_name") == "o4-mini-2025-04-16"
    assert loader.get_value("output.output_dir") == "data/output"
    assert loader.get_value("non_existent_key", "default") == "default"

def test_get_required_columns(mock_config_file):
    """
    Test the get_required_columns method for both tabular and PDF configurations.
    """
    loader = ConfigLoader(mock_config_file)
    
    # Test for tabular columns
    tabular_cols = loader.get_required_columns(is_pdf=False)
    assert tabular_cols == ["id", "title", "abstract"]
    
    # Test for PDF columns
    pdf_cols = loader.get_required_columns(is_pdf=True)
    assert pdf_cols == ["map_id", "text"]

def test_get_output_path(mock_config_file):
    """
    Test the get_output_path method.
    """
    loader = ConfigLoader(mock_config_file)
    assert loader.get_output_path() == "data/output"

def test_get_model_config(mock_config_file):
    """
    Test the get_model_config method.
    """
    loader = ConfigLoader(mock_config_file)
    model_config = loader.get_model_config()
    assert model_config['provider'] == "openai"
    assert model_config['temperature'] == 0.7

def test_file_not_found():
    """
    Test if the loader raises a FileNotFoundError for a non-existent file.
    """
    with pytest.raises(FileNotFoundError):
        ConfigLoader("non_existent_path/config.yaml")

def test_validate_config(mock_config_file):
    """
    Test the validate_config method with a simple schema.
    """
    loader = ConfigLoader(mock_config_file)
    schema = {
        'data_loader': dict,
        'llm_model': dict,
        'output': dict
    }
    assert loader.validate_config(schema) is True
    
    invalid_schema = {'data_loader': str}
    assert loader.validate_config(invalid_schema) is False