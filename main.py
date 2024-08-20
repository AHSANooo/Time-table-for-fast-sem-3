from utils.timetable_scraper import scrape_timetable
from utils.class_finder import find_current_and_next_class


def main():
    # URL to the Google Sheets (your timetable link)
    url = "https://docs.google.com/spreadsheets/d/1XA76yuFM_4mtkQW__2fryUBMe5EZ6XMWtBHxylhV6k8/edit#gid=837984260"

    # Scrape the timetable
    df = scrape_timetable(url)

    # Find the current and next class
    current_class, next_class = find_current_and_next_class(df)

    if current_class is not None:
        print("Current Class:")
        print(current_class)

        if next_class is not None:
            print("\nNext Class:")
            print(next_class)


if __name__ == "__main__":
    main()
