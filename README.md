# generative-ai-text-processing-pipeline
A Python-based pipeline for preprocessing text, generating LLM prompts, and parsing results. Designed for text-based Generative AI workflows.

---

## Features

- **Config Manager**: Centralized configuration for easier customization and scalability.
- **Data Loader**: Load data from PDFs or Excel files into a Pandas DataFrame for processing.
- **Prompt Builder**: Generate structured and optimized prompts for LLMs.
- **API Caller**: Make API calls to LLMs and handle responses.
- **Validator**: Validate JSON format of API responses to ensure data integrity.
- **Data Saver**: Save processed results to CSV and text files.
  
---

## Getting Started

Follow the steps below to set up and run the pipeline.

### Prerequisites

- **Python Version**: Python 3.8 or higher.
- **LLM Access**: API key for a supported LLM provider (e.g., OpenAI, Hugging Face).
- **Dependencies**: Listed in `requirements.txt`.

### Installation

1. Clone the repository:
   ```git clone https://github.com/ashish-som/generative-ai-text-processing-pipeline.git
   cd generative-ai-text-processing-pipeline```

2. Create and activate a virtual environment:
   ```python -m venv env```
```source env/bin/activate  # For Linux/Mac```
```.\env\Scripts\activate   # For Windows```
