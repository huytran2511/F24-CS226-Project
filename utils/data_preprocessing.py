import pandas as pd
import os

def load_and_clean_data(file_path):
    # Load the dataset
    print(f"Loading dataset from {file_path}")
    df = pd.read_csv(file_path, on_bad_lines='skip', low_memory=False)

    # Basic data cleaning (remove null values, convert date columns, etc.)
    df.dropna(inplace=True)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])

    # Save the cleaned dataset for future use
    cleaned_file_path = os.path.join('data', 'cleaned_crime_data.csv')
    df.to_csv(cleaned_file_path, index=False)
    print(f"Cleaned data saved to {cleaned_file_path}")
    return df

if __name__ == "__main__":
    df = load_and_clean_data('data/Chicago_Crimes.csv')