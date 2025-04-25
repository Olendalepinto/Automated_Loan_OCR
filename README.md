# Automated Personal Loan Document Processing Project

This project uses Optical Character Recognition (OCR) to extract relevant information from loan application documents and integrates it with a loan system for further processing.

## Requirements

To set up and run the project, follow the steps below.

### 1. Clone the Repository

Clone the repository from GitHub:

```bash
git clone https://github.com/your-repository-url.git
cd your-repository-folder

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install required libraries
pip install -r requirements.txt

pip install git+https://github.com/madmaze/pytesseract.git

 Running the Frontend
After installing the required libraries and Tesseract, run the frontend UI using Streamlit. Use the following command:

'streamlit run streamlit_app/ui.py'