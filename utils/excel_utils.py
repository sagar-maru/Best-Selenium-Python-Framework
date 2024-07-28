import pandas as pd

def read_excel(file_path, sheet_name):
    try:
        # Ensure the file path is correct and the file exists
        df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None
