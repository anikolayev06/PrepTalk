[![Python Version](https://img.shields.io/badge/python-3.13.5-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Interview Practice AI

Interview Practice AI is a Python desktop application that conducts mock job interviews using AI. It features a graphical user interface (GUI) built with PyQt6, allows you to upload your resume and job description, and provides real-time interview questions with voice recording capabilities. The app uses Gemini AI for generating questions and providing feedback, and Whisper for audio transcription.

## Prerequisites

Before using Interview Practice AI, ensure you have the following:

1. **Python:** The program requires **Python (3.13.5 or newer recommended)**. Download Python from [python.org](https://www.python.org).
2. [Anaconda or Miniconda](https://www.anaconda.com/docs/main) (recommended for managing environments).
3. [Git](https://git-scm.com/install/) (for cloning the repository).
4. A valid **Gemini API Key** from Google AI Studio.
5. **FFmpeg** (required for audio processing with Whisper):
   - Windows: Download from [ffmpeg.org](https://ffmpeg.org/) or install via `choco install ffmpeg`
   - Mac: `brew install ffmpeg`
   - Linux: `sudo apt install ffmpeg`

## Setup

To set up Interview Practice AI, follow these steps:

1. **Clone the repository using git:**

   ```bash
   git clone https://github.com/anikolayev06/PrepTalk.git
   cd PrepTalk
   ```

2. **Create and activate a conda environment (recommended):**

   ```bash
   conda create -n preptalk python=3.13.5
   conda activate preptalk
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Setting Up Your Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/api-keys) and create a Gemini API key.
2. Create a `.env` file in the projects `/backend` directory and add your API key:

   ```
   GEMINI_API_KEY_COMS25=your_api_key_here
   ```

## Usage

To use Interview Practice AI:

1. Run the application:

   ```bash
   python launch.py
   ```

2. Upload your resume (PDF format) using the "Upload Resume" button.
3. Paste or type in the job description you're applying for.
4. Click "Start Interview" to begin the mock interview session.
5. Answer each question by clicking "Start Recording" to record your voice answer.
6. Click "Stop Recording" when finished, and the AI will transcribe and provide feedback.
7. Use "Next Question" to move through the interview questions.

## Features

- **AI-Powered Questions:** Gemini AI generates relevant interview questions based on your resume and job description.
- **Voice Recording:** Record your answers using your microphone for a realistic interview experience.
- **Automatic Transcription:** Whisper AI transcribes your spoken answers to text.
- **Instant Feedback:** Receive AI-generated feedback on your responses.
- **PDF Resume Parsing:** Automatically extracts text from your resume PDF.

## Additional Notes

- The app uses `pdfplumber` to extract text from PDF resumes.
- Audio is recorded using `sounddevice` and transcribed using OpenAI's Whisper model.
- Your API key is stored locally in the `.env` file and never shared.
- Temporary audio recordings are stored in a system temp directory and cleaned up automatically.
- **Be cautious:** AI-generated feedback is based on AI interpretation and may not be 100% accurate.
- Ensure your microphone permissions are enabled for the application to record audio.

## Troubleshooting

- **Recording fails:** Check that your microphone is properly connected and permissions are granted.
- **Transcription errors:** Ensure FFmpeg is installed correctly.
- **API errors:** Verify your Gemini API key is valid and has sufficient quota.

## Credits

Original Authors:
- [an3480-RIT](https://github.com/an3480-RIT)
- [csn1296](https://github.com/csn1296)
- [Maddox-RVS](https://github.com/Maddox-RVS)

## License

This project is licensed under the MIT License with Attribution Requirements. See the [LICENSE](LICENSE) file for details. All forks must include proper attribution to the original authors.