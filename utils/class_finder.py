import pandas as pd
from datetime import datetime

def get_current_time():
    """
    Gets the current time to match it with class timings.
    """
    return datetime.now().time()

def find_current_and_next_class(df):
    """
    Finds the current and next class based on the current time.
    """
    current_time = get_current_time()

    for index, row in df.iterrows():
        class_time = row['Time']  # Adjust based on your CSV structure

        # Convert class_time to time object for comparison
        start_time, end_time = class_time.split('-')
        start_time = datetime.strptime(start_time.strip(), "%H:%M").time()
        end_time = datetime.strptime(end_time.strip(), "%H:%M").time()

        # Check if the current time is within the class duration
        if start_time <= current_time <= end_time:
            current_class = row
            next_class = df.iloc[index + 1] if index + 1 < len(df) else None
            return current_class, next_class

    return None, None
