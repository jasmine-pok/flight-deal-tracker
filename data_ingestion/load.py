import os

def save_to_csv(df):
        departure_date = df["departure"].iloc[0].strftime("%Y-%m-%d")
        file_name = f"flight_deals_{departure_date}.csv"
        folder_path = "data/raw"

        # Create folder if it doesn't exist
        os.makedirs(folder_path, exist_ok=True)

        # Build full path
        file_path = os.path.join(folder_path, file_name)

        # Save the DataFrame
        df.to_csv(file_path, index=False)
        print(f"Saved file to: {file_path}")