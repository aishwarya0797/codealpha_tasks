import os
import re

# Step 1: Define input and output file names
input_file = "input_text.txt"
output_file = "extracted_emails.txt"

# Step 2: Check if input file exists
if not os.path.exists(input_file):
    print(f"Error: '{input_file}' not found.")
    print("Create this file and add some text with email addresses.")
else:
    # Step 3: Read content from input file
    with open(input_file, "r", encoding="utf-8") as file:
        content = file.read()

    # Step 4: Use regex pattern to find email addresses
    # This pattern matches common email formats
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(email_pattern, content)

    # Step 5: Remove duplicates and sort (optional but clean)
    unique_emails = sorted(set(email.lower() for email in emails))

    # Step 6: Write extracted emails to output file
    with open(output_file, "w", encoding="utf-8") as file:
        for email in unique_emails:
            file.write(email + "\n")

    # Step 7: Display result
    if not unique_emails:
        print("No email addresses found.")
    else:
        print(f"Total emails found: {len(unique_emails)}")
        print(f"Emails successfully extracted and saved to '{output_file}'")