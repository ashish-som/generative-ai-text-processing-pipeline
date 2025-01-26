from abc import ABC, abstractmethod
from typing import Any, Dict, List


class PromptBuilderInterface(ABC):
    """
    Abstract base class for building prompts from an Excel sheet.
    This interface ensures that all prompt builder implementations
    adhere to a structure for reading questions and creating a master prompt.
    """

    @abstractmethod
    def load_questions_from_excel(self, excel_path: str) -> List[str]:
        """
        Loads prompt questions from an Excel sheet.

        Args:
            excel_path (str): Path to the Excel file containing prompt questions.

        Returns:
            List[str]: A list of prompt questions.
        """
        pass

    @abstractmethod
    def create_master_prompt(self, questions: List[str], schema: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a master prompt using the questions and the specified schema.

        Args:
            questions (List[str]): A list of prompt questions.
            schema (dict): The JSON schema for structuring the master prompt.

        Returns:
            dict: The master prompt in the specified JSON schema.
        """
        pass

    @abstractmethod
    def validate_prompt(self, prompt: Dict[str, Any], schema: Dict[str, Any]) -> bool:
        """
        Validates the created master prompt against the given JSON schema.

        Args:
            prompt (dict): The master prompt to be validated.
            schema (dict): The JSON schema for validation.

        Returns:
            bool: True if the prompt is valid according to the schema, False otherwise.
        """
        pass
