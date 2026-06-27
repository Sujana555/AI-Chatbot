AI-Chatbot: Syllabus Understanding Assistant

A simple AI-powered chatbot that helps students understand their course syllabus. Upload a syllabus PDF, ask questions about it in plain English, and get answers grounded in the actual document — due dates, grading breakdowns, policies, and more.

Features


PDF text extraction — pulls text content from a syllabus PDF using PyMuPDF
AI-powered Q&A — ask natural language questions and get answers based on the syllabus content
Custom personality — configurable tone and behavior via a system prompt
Simple CLI chat loop — interactive terminal-based conversation


How It Works


The syllabus PDF is loaded once at startup and its text is extracted.
Each time you ask a question, the chatbot sends the syllabus text + your question + a system prompt to the AI model.
The model answers strictly based on the syllabus content, and says so if the answer isn't in the document.


Tech Stack


Python 3
PyMuPDF (fitz) — PDF text extraction
OpenAI Python SDK — used via OpenRouter as the API gateway
python-dotenv — environment variable management


Project Structure

AI-Chatbot/
├── .venv/                 # Virtual environment (not tracked in git)
├── .env                   # API keys (not tracked in git)
├── main.py                # Entry point — chat loop & AI integration
├── document_handler.py    # PDF text extraction logic
└── README.md

Setup

1. Clone the repo

bashgit clone <your-repo-url>
cd AI-Chatbot

2. Create and activate a virtual environment

bashpython -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # macOS/Linux

3. Install dependencies

bashpip install pymupdf openai python-dotenv

4. Set up your environment variables

Create a .env file in the project root:

OPENROUTER_API_KEY=your_api_key_here

5. Add your syllabus

Place a syllabus PDF in the project root and update the syllabus_path variable in main.py to match its filename.

Usage

Run the chatbot:

bashpython main.py

Then just ask questions:

You: When is the midterm exam?
Chatbot: According to the syllabus, the midterm exam is on...

You: How much is attendance worth?
Chatbot: Attendance counts for 10% of your final grade.

Type quit, exit, or bye to end the session.

Current Limitations


Supports a single PDF syllabus loaded at startup (no multi-file or runtime upload yet)
No graphical/web interface — terminal only
No persistent memory across sessions
Very long syllabi may exceed the model's context window
Scanned/image-based PDFs (no text layer) won't extract correctly


Roadmap (Future Polish)

 Support different type of document.
 Web-based chatbot.
 Web-based file upload interface
 Better error handling for malformed/scanned PDFs
 Multi-syllabus support (e.g., one per course)
 Persistent chat history


License

This project is for personal/educational use.
