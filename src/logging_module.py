"""
Description: General logging module. This module is used to log messages to the console and to a file.
The log file is created inside the log directory and it is named as the name of the script that is running.

This module can be used by importing in any script.
"""
import logging
import os

def logger():
    """This function creates a logger object that can be used to log messages to the console and to a file.
    """
    # create a custom logger
    logger = logging.getLogger(__name__)
    logger.setLevel("DEBUG")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(lineno)d')

    # configure the logging to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel("DEBUG")
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # configure the logging to the file
    
    # Check if the log directory exists
    current_path = os.getcwd()
    log_folder = os.path.join(current_path, "..", "logs")
    logger.info(f"logs folder path: {log_folder}")
    
    
    base_file = os.path.basename(__file__) + ".log"
    logger.info(f"Base file: {base_file}")
    
    log_file_path = os.path.join(log_folder, base_file)
    if not os.path.exists(log_file_path):
        with open(log_file_path, "w") as file:
            file.write("Log file created")
        
    file_handler = logging.FileHandler(os.path.join("logs", base_file))
    file_handler.setLevel("DEBUG")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

def create_log_folder(logger):
    """This function creates a log file inside the log directory.
    """
    # Check if the log directory exists
    current_path = os.getcwd()
    logger.info(f"Current path: {current_path}")
    # Move up a directory and create a logs directory. If it already exists, do nothing.
    try:
        os.makedirs(os.path.join(current_path, "..", "logs"))
    except FileExistsError:
        pass
         
         
if __name__ == "__main__":
    # call logger function
    logger = logger()
    
    # Create log folder
    create_log_folder(logger)  
    
    
    

