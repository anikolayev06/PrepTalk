from typing import Optional
from google import genai
from pathlib import Path

GEMINI_MODEL = "gemini-2.5-flash"

class Conversation:
    def __init__(self):
        self.client = genai.Client()
        self.chat = self.client.chats.create(model=GEMINI_MODEL)

    def prompt_gemini(input: str) -> Optional[str]:
        """
        Send a prompt to the Gemini model and return the text response if successful.

        Parameters
        ----------
        input : str
            The prompt text to send to Gemini.

        Returns
        -------
        Optional[str]
            The text response from Gemini on success, or None on failure.
        """

        pass

    def submit_pdf(prompt: str, pdf_path: Path) -> bool:
        """
        Submit a resume PDF for processing.

        Parameters
        ----------
        pdf_path : Path
            The path to the PDF file to submit.

        Returns
        -------
        bool
            True if the submission was successful, False otherwise.
        """

        pass