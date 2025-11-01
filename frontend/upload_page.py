from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit, QFileDialog
from PyQt6.QtCore import Qt
import os

class UploadPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.resume_path = None

        layout = QVBoxLayout()

        self.resume_label = QLabel("No resume selected.")
        layout.addWidget(self.resume_label)

        upload_button = QPushButton("Upload Resume (PDF)")
        upload_button.clicked.connect(self.select_pdf)
        layout.addWidget(upload_button, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(QLabel("Paste the job description:"))
        self.job_input = QTextEdit()
        self.job_input.setPlaceholderText("Paste the job description here...")
        layout.addWidget(self.job_input)

        start_button = QPushButton("Start Interview")
        start_button.clicked.connect(self.start_interview)
        layout.addWidget(start_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def select_pdf(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("PDF files (*.pdf)")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                self.resume_path = selected_files[0]
                filename = os.path.basename(self.resume_path)
                self.resume_label.setText(f"Selected resume: {filename}")
                print(f"Selected PDF path: {self.resume_path}")

    def start_interview(self):
        job_text = self.job_input.toPlainText()

        if not self.resume_path:
            self.resume_label.setText("Please upload a resume before starting.")
            return

        resume_text = self.resume_path

        if self.parent:
            self.parent.start_interview(resume_text, job_text)