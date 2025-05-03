import pandas as pd
import faker as faker

# Function to print the banner for the application
def print_banner():
    print("=" * 63)
    print("         🔎 Redback Dummy Data Generator v1.0")
    print("=" * 63)
    print("\n Welcome to the Redback Dummy Data Generator!")
    print(" This tool generates realistic test files containing")
    print(" synthetic sensitive data for scanner testing purposes.\n")
    print("-" * 63)

# Function to get the file types the user wants to generate
def get_file_types():
    print(" Please choose the file type(s) to generate:")
    print(" [1] CSV (.csv)")
    print(" [2] JSON (.json)")
    print(" [3] Text (.txt)")
    print(" [4] Word Document (.docx)")
    print(" [5] PDF (.pdf)")
    print(" [6] Source Code (.py, .yaml, .env)")
    print(" [7] All of the above")
    while True:
        # Prompt user for input and validate it
        choice = input(" Enter your choice (e.g., 1 or 3,5 or 7): ").strip()
        if choice and all(c in "1234567," for c in choice.replace(" ", "")):
            return choice  # Return valid input
        print(" Invalid input. Please enter a valid choice (e.g., 1 or 3,5 or 7).")

# Function to get the sensitivity level of the data
def get_sensitivity_level():
    print("-" * 63)
    print(" Select data sensitivity level:")
    print(" [1] Low (Public or non-sensitive)")
    print(" [2] Medium (Internal-use PII/NPI)")
    print(" [3] High (Critical PII, PHI, Financial, Secrets)")
    print(" [4] Mixed (Randomised levels)")
    while True:
        # Prompt user for input and validate it
        level = input(" Enter your choice: ").strip()
        if level in {"1", "2", "3", "4"}:
            return level  # Return valid input
        print(" Invalid input. Please enter a number between 1 and 4.")

# Function to get the number of files to generate
def get_number_of_files():
    print("-" * 63)
    while True:
        # Prompt user for input and validate it
        count = input(" Enter number of sample files to generate: ").strip()
        if count.isdigit() and int(count) > 0:
            return int(count)  # Return valid input as an integer
        print(" Invalid input. Please enter a positive integer.")

# Function to print a summary of the user's selections
def print_summary(file_types, sensitivity, count):
    print("-" * 63)
    print(" Summary of your selections:")
    print(f"    - File types selected: {file_types}")
    print(f"    - Sensitivity level: {sensitivity}")
    print(f"    - Total files: {count}")
    print("-" * 63)
    print(" No files have been generated. This is a UI skeleton only.")
    print("=" * 63)
    print(" Thank you for using the Redback Dummy Data Generator!")
    print("=" * 63)

# Main function to handle the console-based user interface
def console_ui():
    print_banner()  # Display the banner
    file_types = get_file_types()  # Get file types from the user
    sensitivity = get_sensitivity_level()  # Get sensitivity level from the user
    count = get_number_of_files()  # Get the number of files to generate
    print_summary(file_types, sensitivity, count)  # Print a summary of the selections
    return file_types, sensitivity, count  # Return the collected inputs
