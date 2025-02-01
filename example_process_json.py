"""
Process a JSON file to count state fair ribbons by county and save the result.

"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import json

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name: str = r"C:\Projects\datafun-03-analytics\datafun-03-analytics\example-data"
processed_folder_name: str = "example_processed"

#####################################
# Define Functions
#####################################

def count_ribbons_by_county(file_path: pathlib.Path) -> dict:
    """Count the number of state fair ribbons awarded by county from a JSON file."""
    
    county_ribbon_counts = {}

    try:
         # Open and read the JSON file
        with file_path.open('r') as file:
                ribbon_data = json.load(file)  # Load JSON data into a Python dictionary
            
            # Extract the list of "top" items from the JSON data
                top_list = ribbon_data.get("top", [])
            
            # Loop through each record in the "top" list
        for entry in top_list:
                county = entry.get("item", "Unknown")  # Get the county (use "Unknown County" if missing)
                # Increment the ribbon count for this county
                county_ribbon_counts[county] = county_ribbon_counts.get(county, 0) + 1
            
        return county_ribbon_counts  # Return the dictionary of county ribbon counts

    except Exception as e:
        # Log any error that occurs during the process
        logger.error(f"Error reading or processing JSON file: {e}")
        return {}  # Return an empty dictionary if error occurs

def process_json_file():
    """Read a JSON file, count ribbons, and save the result."""
    # Set the path for the input JSON file and the output text file
    input_file = pathlib.Path(fetched_folder_name, "state-fair.json")
    output_file = pathlib.Path(processed_folder_name, "state-fair-ribbon.txt")
    
    # Call the function to count ribbons by county
    ribbon_counts = count_ribbons_by_county(input_file)
    
    # Ensure the output folder exists
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Write the results to the output text file
    with output_file.open('w') as file:
        file.write("Fair Ribbons by County:\n")
        for county, count in ribbon_counts.items():  # Iterate over the dictionary returned by the function
            file.write(f"{county}: {count}\n")
    
    # Log that the file was processed and results saved
    logger.info(f"Processed JSON file: {input_file}, Results saved to: {output_file}")



#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")
