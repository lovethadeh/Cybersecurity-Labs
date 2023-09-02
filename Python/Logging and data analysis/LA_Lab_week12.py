#   NAME      Loveth Adeh
#   id        1153017
#   FUNCTION  lab 10 
#             Python 3.11
#             WING Personal 9.0.2
#   date      Summer 2023 (31 July 2023)
#   ======================================
import datetime
import logging
import platform

# Step 1: Defining the filenames
initials = "LA"  # Replace with your initials
output_txt_filename = f"{initials}_Lab10_output.txt"
output_log_filename = f"{initials}_Lab10_output.log"

# Step 2: Initializing the logging
logging.basicConfig(filename=output_log_filename, level=logging.INFO, filemode='w')
logging.info("6079 Lab 10 – Logging Information")
logging.info("Due July 30, 2023 11:59 pm")

# Step 3: Creating variables using strftime()
current_date_with_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
current_date_no_time = datetime.datetime.now().strftime("%Y%m%d")

# Step 4: Retrieving PC data and write to the text file
pc_info = [
    f"Machine: {platform.machine()}",
    f"Version: {platform.version()}",
    f"Platform: {platform.platform()}",
    f"System: {platform.system()}",
    f"Processor: {platform.processor()}"
]

with open(output_txt_filename, "w") as file:
    file.write("PC Information:\n")
    file.write("\n".join(pc_info))

# Step 5: Using try-except to handle exceptions
try:
    # Add code here that may raise exceptions
    result = 10 / 0  # Example division by zero to raise an exception
except Exception as ex:
    logging.error(f"PC Info Data Error: {str(ex)}")

# Step 6: Writing down the data to the log file
try:
    # Add code here to perform some operations
    logging.info("Logging completed successfully.")
except Exception as ex:
    logging.error(f"Error occurred during logging: {str(ex)}")

# Step 7: Display "completed"
print("Completed")
