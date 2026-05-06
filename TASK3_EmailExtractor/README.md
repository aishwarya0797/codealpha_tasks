# Task 3: Email Extractor 

##  Description

This project is a Python program that extracts all email addresses from a text file using regular expressions and saves them into a separate output file.

##  Features

* Reads data from a `.txt` file
* Uses regex to extract valid email addresses
* Removes duplicate emails
* Converts emails to lowercase for consistency
* Saves extracted emails into a new file
* Displays total number of emails found

##  Technologies Used

* Python
* Regular Expressions (`re` module)
* File Handling (`os` module)

##  How to Run

1. Ensure `input_text.txt` file exists in the same folder
2. Add sample text containing email addresses
3. Open terminal in the project folder
4. Run the file:

   ```bash
   python email_extractor.py
   ```

##  How It Works

* Checks if input file exists
* Reads file content
* Uses regex pattern to find email addresses
* Removes duplicates using `set()`
* Sorts and saves results to `extracted_emails.txt`

##  File Structure

* email_extractor.py → Main program
* input_text.txt → Input file
* extracted_emails.txt → Output file

##  Outcome

This project demonstrates the use of regular expressions, file handling, and data processing techniques in Python.
