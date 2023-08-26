Smart Toll Collection System
This Python program automates the process of toll collection using image processing, Optical Character Recognition (OCR), and SMS notifications. It detects license plates, extracts information, communicates with a MySQL database, and sends SMS notifications to users.

Prerequisites
Python 3.x
OpenCV (cv2)
Tesseract OCR
MySQL Server
Way2SMS API Credentials
Installation
Clone this repository or download the code files.
Install the required Python libraries using the following command:
Copy code
pip install opencv-python pytesseract requests
Setup
Haar Cascade Classifier XML File:

The program references a Haar Cascade classifier XML file named 'cascade.xml'. This file is used for face detection. Ensure you have the file available.
Tesseract OCR:

Install Tesseract OCR on your system.
Set the path to the Tesseract executable in the code: pytesseract.pytesseract.tesseract_cmd = r"path/to/tesseract.exe"
MySQL Database:

Set up a MySQL server.
Create a database named "car" and define the necessary tables (e.g., "plate").
Update the database credentials in the code: host, user, passwd, database.
Way2SMS API Credentials:

Sign up for a Way2SMS account to obtain API credentials (API key and secret key).
Update the API credentials in the code: apiKey, secretKey.
Usage
Place the Haar Cascade classifier XML file (cascade.xml) in the program directory.
Run the program using Python:

python final.py
The program will process images, detect license plates, extract information, update the database, and send SMS notifications.
Important Note
 Always ensure that you have proper permissions to use external services and resources like the Way2SMS API.