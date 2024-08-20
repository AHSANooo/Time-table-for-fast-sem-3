from auth import authenticate_google_sheets
from data_operations import save_to_csv, save_to_excel, load_csv, load_excel
from timetable_operations import get_current_and_next_class
from datetime import datetime
import pandas as pd


def fetch_timetable(sheet):
    data = {}
    for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:  # Assuming each day has a separate sheet
        worksheet = sheet.worksheet(day)
        data[day] = pd.DataFrame(worksheet.get_all_records())
    return data


def main():
    # Step 1: Authenticate and fetch timetable from Google Sheets
    sheet = authenticate_google_sheets()
    timetable_data = fetch_timetable(sheet)

    # Step 2: Save timetable to CSV or Excel
    save_to_csv(timetable_data)  # Optionally, you can use save_to_excel(timetable_data)

    # Step 3: Load today's timetable
    current_day = datetime.now().strftime('%A')
    df = load_csv(current_day)  # Or use load_excel(current_day)

    if df is not None:
        # Step 4: Find current and next class
        current_class, next_class = get_current_and_next_class(df)

        if current_class is not None:
            print(
                f"Current Class: {current_class['Class']} in Room {current_class['Room']} from {current_class['Start Time']} to {current_class['End Time']}")
        else:
            print("No current class found.")

        if next_class is not None:
            print(f"Next Class: {next_class['Class']} in Room {next_class['Room']} at {next_class['Start Time']}")
        else:
            print("No next class found.")
    else:
        print("No data available for today.")


if __name__ == "__main__":
    main()
