import pandas as pd
import os

# Save each day's timetable to a separate CSV file
def save_to_csv(timetable_data):
    for day, df in timetable_data.items():
        df.to_csv(f"{day}.csv", index=False)
    print("Timetable saved to CSV files.")

# Save all timetables into a single Excel file with multiple sheets
def save_to_excel(timetable_data):
    with pd.ExcelWriter('timetable.xlsx') as writer:
        for day, df in timetable_data.items():
            df.to_excel(writer, sheet_name=day, index=False)
    print("Timetable saved to Excel.")

# Load a specific day's CSV
def load_csv(day):
    file_path = f"{day}.csv"
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        print(f"CSV file for {day} not found.")
        return None

# Load a specific day's sheet from the Excel file
def load_excel(day):
    file_path = "timetable.xlsx"
    if os.path.exists(file_path):
        return pd.read_excel(file_path, sheet_name=day)
    else:
        print(f"Excel file not found.")
        return None
