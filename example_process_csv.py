"""
Process a CSV file to show which state had the lowest temperatue for December 2024
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import csv
import statistics
import datetime

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name: str = "example-data"
processed_folder_name: str = "example-processed-data"

#####################################
# Define Functions
#####################################

def find_lowest_temp_for_states(file_path, start_date, end_date):
    """Find the lowest temperature for each state within the specified date range."""

    # Convert input dates to datetime objects for easy comparison
    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')

    # Initialize a dictionary to store the lowest temperature for each state
    lowest_temps = {}

    # Open the CSV file and read its content
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        
        # Loop through each row (state) in the CSV file
        for row in csv_reader:
            state = row['State'].strip()  # Assuming 'State' is the column with state names

            # Initialize variables for tracking the lowest temperature for this state
            lowest_temp = float('inf')
            lowest_temp_date = None
            
            # Loop through the date columns in the row (assuming the columns are dates)
            for date_str, temp_str in row.items():
                # Skip the 'State' column and check only the date columns
                if date_str == 'State':
                    continue

                # Convert the date_str into a datetime object for comparison
                try:
                    date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
                except ValueError:
                    # If the date is not in the expected format, skip this column
                    continue
                
                # Check if the date is within the range
                if start_date <= date <= end_date:
                    try:
                        # Get the temperature and compare with the lowest found so far
                        temp = float(temp_str)
                        if temp < lowest_temp:
                            lowest_temp = temp
                            lowest_temp_date = date_str
                    except ValueError:
                        # Skip rows where the temperature is not a valid number
                        continue
            
            # After checking all dates, store the result for the state
            if lowest_temp != float('inf'):
                lowest_temps[state] = (lowest_temp, lowest_temp_date)

    # Return the dictionary of lowest temperatures for each state
    return lowest_temps


def process_csv_file():
    """Read a CSV file, find which state had the lowest temp for December 2024, and save the results."""
    
    # Define the input and output file paths
    input_file = pathlib.Path(fetched_folder_name, "C:\Projects\datafun-03-analytics\example-data\daily-temps-dec24.csv")
    output_file = pathlib.Path(processed_folder_name, "C:\Projects\datafun-03-analytics\datafun-03-analytics\example-processed-data")
    
    # Make sure the output folder exists
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Define the date range for December 2024
    start_date = "2024-12-01"
    end_date = "2024-12-31"
    
    # Process the CSV to find the minimum temperature for each state in December 2024
    lowest_temps = find_lowest_temp_for_states(input_file, start_date, end_date)
    
    # Write the results to the output file
    with output_file.open('w') as file:
        file.write(f"Lowest Temperature for Each State between {start_date} and {end_date}:\n")
        for state, (temp, date) in lowest_temps.items():
            file.write(f"{state}: {temp}° on {date}\n")
    
    logger.info(f"Processed CSV file: {input_file}, Results saved to: {output_file}")


# Main Execution
if __name__ == "__main__":
    logger.info("Starting CSV processing...")
    process_csv_file()
    logger.info("CSV processing complete.")

