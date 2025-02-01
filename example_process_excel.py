"""
Process an Excel file to count occurrences of a Full Moon.

"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib

# Import from external packages
import openpyxl


# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name: str = "C:\Projects\datafun-03-analytics\datafun-03-analytics\example-data"
processed_folder_name: str = "example-processed-data"

#####################################
# Define Functions
#####################################

def count_word_in_column(file_path: pathlib.Path, column_letter: str, word: str) -> int:
    """Count the occurrences of a specific word in a given column of an Excel file."""
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        count = 0
        for cell in sheet[column_letter]:
            if cell.value and isinstance(cell.value, str):
                count += cell.value.lower().count(word.lower())
        return count
    except Exception as e:
        logger.error(f"Error reading Excel file: {e}")
        return 0

def process_excel_file():
    """Read an Excel file, count occurrences of "Full Moon" in a specific column, and save the result."""
    input_file = pathlib.Path(fetched_folder_name, "C:\Projects\datafun-03-analytics\datafun-03-analytics\example-data\day-forecast.xlsx")
    output_file = pathlib.Path(processed_folder_name, "excel_processed_fullmoon_count.txt")
    column_to_check = "G"  # Replace with the appropriate column letter
    word_to_count = "Full Moon"
    word_count = count_word_in_column(input_file, column_to_check, word_to_count)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open('w') as file:
        file.write(f"Occurrences of '{word_to_count}' in column {column_to_check}: {word_count}\n")
    logger.info(f"Processed Excel file: {input_file}, Word count saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting Excel processing...")
    process_excel_file()
    logger.info("Excel processing complete.")
