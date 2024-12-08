import pandas as pd
import matplotlib.pyplot as plt

# Function to load the data from the CSV file
def load_data(file_name="applications.csv"):
    """
    Load data from the specified CSV file.
    Args:
        file_name (str): Path to the CSV file.
    Returns:
        DataFrame: The loaded data as a pandas DataFrame.
    """
    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(file_name)

        # Clean column names
        df.columns = df.columns.str.strip()  # Remove spaces
        df.columns = df.columns.str.title()  # Title case for consistency

        # Ensure the 'Date' column is parsed as datetime
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # Convert to datetime, handling errors
        else:
            print("Warning: 'Date' column is missing from the CSV file.")

        return df
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
        return pd.DataFrame()  # Return an empty DataFrame if the file is not found
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return pd.DataFrame()


# Example usage
if __name__ == "__main__":
    # Path to the CSV file
    file_path = "applications.csv"  # Ensure the file name matches your CSV file

    # Load the data
    df = load_data(file_path)

    # Print loaded data and columns for debugging
    print(df.head())
    print(df.columns)

    # Analysis functions
    def show_status_counts(data):
        """
        Display a bar chart of application status counts.
        """
        if 'Status' not in data.columns:
            print("Error: 'Status' column is missing in the data.")
            return

        if data.empty:
            print("No data available for analysis.")
            return

        status_counts = data['Status'].value_counts()
        plt.figure(figsize=(8, 6))
        status_counts.plot(kind='bar', color='skyblue')
        plt.title("Application Status Count")
        plt.xlabel("Status")
        plt.ylabel("Number of Applications")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # Call the analysis function
    show_status_counts(df)
