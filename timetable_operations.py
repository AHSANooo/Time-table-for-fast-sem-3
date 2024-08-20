from datetime import datetime


def get_current_and_next_class(df):
    current_time = datetime.now().time()

    for index, row in df.iterrows():
        # Assuming 'Start Time' and 'End Time' columns exist
        start_time = datetime.strptime(row['Start Time'], '%H:%M').time()
        end_time = datetime.strptime(row['End Time'], '%H:%M').time()

        if start_time <= current_time <= end_time:
            current_class = row
            next_class = df.iloc[index + 1] if index + 1 < len(df) else None
            return current_class, next_class

    return None, None
