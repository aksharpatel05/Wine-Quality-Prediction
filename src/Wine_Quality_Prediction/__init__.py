import os  # Provides functions to interact with the operating system
import sys  # Used to handle system-specific parameters
import logging  # Provides logging capabilities

#Defining the Log Format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

#Creating a Directory for Logs
log_dir = "logs"  # Directory name for logs
log_filepath = os.path.join(log_dir, "logging.log")  # Path to log file
os.makedirs(log_dir, exist_ok=True)  # Create the directory if it doesn't exist

#Configuring Logging
logging.basicConfig(
    level=logging.INFO,  # Sets the logging level to INFO
    format=logging_str,  # Uses the predefined log format
    handlers=[
        logging.FileHandler(log_filepath),  # Logs messages to a file
        logging.StreamHandler(sys.stdout)   # Prints logs to the console
    ]
)

#Creating a Logger Object
logger = logging.getLogger("project_logger")
