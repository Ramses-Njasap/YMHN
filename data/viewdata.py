import os
import pandas as pd

def load_csv(filename):
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)
    
    # Load the CSV using Pandas
    data = pd.read_csv(file_path)
    return data

def main():
    # Define the filename
    filename = 'nvdrs-data-export.csv'
    
    # Load data and display the first few rows
    data = load_csv(filename)
    print(data.head())

# Ensures the script runs only when executed directly
if __name__ == "__main__":
    main()