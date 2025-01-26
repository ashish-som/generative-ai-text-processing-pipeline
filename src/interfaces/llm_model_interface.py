from abc import ABC, abstractmethod
from typing import Any, Dict


class LLMModelInterface(ABC):
    """
    Abstract base class for interacting with LLM APIs.
    This interface ensures all LLM model client implementations
    follow a standard structure for sending requests and processing responses.
    """

    @abstractmethod
    def make_request(self, prompt: str, model: str, temperature: float = 0.5, max_tokens: int = 500) -> Dict[str, Any]:
        """
        Sends a request to the LLM model with the given parameters.

        Args:
            prompt (str): The text input or query to be processed by the model.
            model (str): The name of the LLM model to be used (e.g., 'gpt-3.5-turbo').
            temperature (float, optional): Sampling temperature, controlling randomness. Defaults to 0.7.
            max_tokens (int, optional): The maximum number of tokens to generate. Defaults to 150.

        Returns:
            dict: The response from the LLM model, containing generated text and metadata.
        """
        pass

    @abstractmethod
    def handle_response(self, response: Dict[str, Any]) -> str:
        """
        Processes the response from the LLM API and extracts the relevant output.

        Args:
            response (dict): The API response, typically containing 'choices' and 'text'.

        Returns:
            str: The generated text from the LLM model.
        """
        pass
