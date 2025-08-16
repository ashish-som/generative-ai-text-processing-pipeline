import os
import pandas as pd
import pytest
import fitz  # PyMuPDF
from src.data_loader.data_loader import DataLoader

@pytest.fixture
def dummy_csv_file(tmp_path):
    """Create a dummy CSV file for testing."""
    data = pd.DataFrame({
        'id': [1, 2, 3],
        'title': ['title-1', 'title-2', 'title-3'],
        'abstract': ['abstract-1', 'abstract-2', None]
    })
    csv_file = tmp_path / "dummy_data.csv"
    data.to_csv(csv_file, index=False)
    return csv_file

@pytest.fixture
def dummy_excel_file(tmp_path):
    """Create a dummy Excel file for testing."""
    data = pd.DataFrame({
        'id': [1, 2, 3],
        'title': ['T-1', 'T-2', 'T-3'],
        'abstract': ['Ab-1', 'Ab-2', 'Ab-3']
    })
    excel_file = tmp_path / "dummy_data.xlsx"
    data.to_excel(excel_file, index=False)
    return excel_file

@pytest.fixture
def dummy_pdf_file(tmp_path):
    """Create a dummy PDF file for testing."""
    file_path = tmp_path / "dummy_doc.pdf"
    doc = fitz.open()  # new PDF
    page = doc.new_page()
    page.insert_text((72, 72), "This is a test PDF document for data loading.")
    doc.save(file_path)
    doc.close()
    return str(file_path)

DUMMY_PDF_PATH = os.path.join(
    os.path.dirname(__file__),
    "dummy_data.pdf"
)

def test_load_csv(dummy_csv_file):
    """Test loading a CSV file."""
    loader = DataLoader(str(dummy_csv_file))
    data = loader.load_data()
    assert not data.empty
    assert 'id' in data.columns
    assert 'title' in data.columns
    assert 'abstract' in data.columns

def test_load_excel(dummy_excel_file):
    """Test loading an Excel file."""
    loader = DataLoader(str(dummy_excel_file))
    data = loader.load_data()
    assert not data.empty
    assert 'id' in data.columns
    assert 'title' in data.columns
    assert 'abstract' in data.columns

def test_validate_columns_csv(dummy_csv_file):
    """Test validating required columns in a CSV file."""
    loader = DataLoader(str(dummy_csv_file))
    loader.load_data()
    required_columns = ['id', 'title', 'abstract']
    assert loader.validate_columns(required_columns) is True

def test_validate_columns_excel(dummy_excel_file):
    """Test validating required columns in an excel."""
    loader = DataLoader(str(dummy_excel_file))
    loader.load_data()
    required_columns = ['id', 'title', 'abstract']
    assert loader.validate_columns(required_columns) is True

def test_load_pdf():
    """Test loading a PDF file."""
    loader = DataLoader(DUMMY_PDF_PATH)
    data = loader.load_data()
    assert not data.empty
    assert 'map_id' in data.columns
    assert 'text' in data.columns
    assert isinstance(data, pd.DataFrame)
    assert data.iloc[0]['map_id'] == "dummy_data"
    assert len(data.iloc[0]['text']) > 0
