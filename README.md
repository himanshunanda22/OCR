# Flask OCR Web Application

This is a Flask web application that allows users to upload images and perform Optical Character Recognition (OCR) on them. The application uses the EasyOCR library for text recognition and annotates the uploaded images with bounding boxes and recognized text.
![image](https://github.com/himanshunanda22/OCR/assets/69206689/1378e216-a9e3-4c9d-9203-e59fc6f66168)

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.x
- Pip (Python package manager)

## Setup

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/flask-ocr-app.git
Navigate to the project directory:

bash
Copy code
cd flask-ocr-app
Create a virtual environment (recommended):

bash
Copy code
python -m venv venv
Activate the virtual environment:

**On Windows:**

bash
Copy code
venv\Scripts\activate
On macOS and Linux:

bash
Copy code
source venv/bin/activate
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Run the Flask application:

bash
Copy code
python app.py
The application will be accessible at http://localhost:5000 in your web browser.

**Usage**
Access the application in your web browser.

Click on the "Choose File" button to upload an image (supported formats: .jpg, .png, .jpeg).

Click the "Upload and OCR" button to perform OCR on the uploaded image.

The OCR results, including recognized text and annotated image, will be displayed on the web page.

You can switch between light and dark themes using the theme toggle.

**File Structure**
flask-ocr-app/                 # Root directory
│
├── app.py                     # Main Flask application
│
├── static/                    # Static files (CSS, images)
│   ├── css/
│   │   └── style.css          # CSS styles for the web app
│   ├── images/
│   │   ├── gitlogo.svg        # GitHub logo image
│   │   ├── leetlogo.ico       # LeetCode logo image
│   │   └── uploads/           # Uploaded images (auto-generated)
│   └── ...                    # Other static files
│
├── templates/                 # HTML templates
│   ├── index.html             # Main HTML template for the web app
│   └── ...                    # Other HTML templates (if any)
│
├── uploads/                   # Uploaded images (auto-generated)
│
├── README.md                  # Readme file with project documentation
│
├── requirements.txt           # List of Python dependencies
│
└── venv/                      # Virtual environment (created when using venv)

