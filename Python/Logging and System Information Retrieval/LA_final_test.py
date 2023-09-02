import os
import platform
from datetime import datetime

# Create a log file
log_file = open("log.txt", "w")

# Insert name and Student ID
name = "LOVETH ADEH"
student_id = "1153017"
log_file.write(f"Name: {name}\nStudent ID: {student_id}\n")

# Insert programmed Current Date
current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_file.write(f"Current Date: {current_date}\n")

# Read data from a text file and insert into the log file
with open("Ladeh_final_test.txt", "r") as text_file:
    data = text_file.read()
    log_file.write("\nData from text file:\n")
    log_file.write(data)

log_file.close()
class MyClass:
    def __init__(self, value):
        self._value = value

    def add_number(self):
        total = 0
        while True:
            try:
                num = float(input("Enter a number (press Enter to finish): "))
                if not num:
                    break
                total += num
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        print(f"Total sum: {total}")

# Print Current Working Directory (CWD)
print("Current Working Directory:", os.getcwd())

# Print files and directories in the current Directory
print("Files and Directories in Current Directory:")
for item in os.listdir():
    print(item)

# Create an instance of MyClass and use it
my_instance = MyClass(10)
my_instance.add_number()

# Retrieve Laptop OS information
os_info = platform.system() + " " + platform.release()

# Write OS information to the log file
with open("log.txt", "a") as log_file:
    log_file.write(f"OS Information: {os_info}\n")

# Retrieve current version of Python
python_version = platform.python_version()

# Write Python version to the log file
with open("log.txt", "a") as log_file:
    log_file.write(f"Python Version: {python_version}\n")

# Create a new folder
new_folder_name = "new_folder"
os.makedirs(new_folder_name)

# Write folder name to the log file
with open("log.txt", "a") as log_file:
    log_file.write(f"New Folder Created: {new_folder_name}\n")

