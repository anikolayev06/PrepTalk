"""
Main application window for PrepTalk frontend.

This module was developed with assistance from AI tools (GitHub Copilot/Claude).
AI was used for code generation, documentation, debugging, and optimization.

Date: November 2, 2025
AI Assistant: GitHub Copilot (Claude Sonnet 4.5)
"""

from PyQt6.QtWidgets import QMainWindow, QStackedWidget
from frontend.upload_page import UploadPage
from frontend.interview_page import InterviewPage

class MainWindow(QMainWindow):
    """
    Main window class for PrepTalk, manages page navigation.
    """

    def __init__(self):
        """
        Initialize the main window and set up page stack.
        """
        super().__init__()
        self.setWindowTitle("PrepTalk")
        self.setGeometry(100, 100, 600, 400)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.upload_page = UploadPage(self)
        self.interview_page = InterviewPage(self)

        self.stack.addWidget(self.upload_page)
        self.stack.addWidget(self.interview_page)

        self.stack.setCurrentWidget(self.upload_page)

    def start_interview(self, resume_text, job_text):
        """
        Transition to the interview page, loading the resume and job description.

        Parameters
        ----------
        resume_text : str
            The candidate's resume text or path.
        job_text : str
            The job description text.
        """
        self.interview_page.load_interview(resume_text, job_text)
        self.stack.setCurrentWidget(self.interview_page)