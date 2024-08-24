import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# URL of Google Sheets
url = 'https://docs.google.com/spreadsheets/d/1XA76yuFM_4mtkQW__2fryUBMe5EZ6XMWtBHxylhV6k8/htmlview?gid=837984260#'


def scrape_timetable(url):
    # Initialize WebDriver
    driver = webdriver.Firefox()
    driver.get(url)

    # Wait for the page to load
    #time.sleep(5)

    # Find the sheet buttons
    sheet_buttons = driver.find_elements(By.CSS_SELECTOR, 'li[id^="sheet-button"] a')

    if not sheet_buttons:
        print("No sheet buttons found.")
        driver.quit()
        return

    print(f"Found {len(sheet_buttons)} sheet buttons.")

    all_sheets_data = {}

    # Loop through each sheet button and click it
    for button in sheet_buttons:
        sheet_name = button.text
        print(f"Switching to sheet: {sheet_name}")

        try:
            button.click()
            #time.sleep(3)  # Wait for the sheet to load

            # Parse the new sheet content
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            # Data containers
            data = []

            # Correctly identify class name, room number, and time columns
            course_names = soup.find_all('td', class_='s5')  # Adjust class if necessary
            room_numbers = soup.find_all('td', class_='s39')  # Adjust class if necessary
            times = soup.find_all('td', class_='s38')  # Adjust class if necessary

            # Loop through and match each row
            for i in range(len(course_names)):
                row = {
                    'Course Name': course_names[i].get_text(strip=True),
                    'Room Number': room_numbers[i].get_text(strip=True) if i < len(room_numbers) else 'N/A',
                    'Time': times[i].get_text(strip=True) if i < len(times) else 'N/A'
                }
                data.append(row)

            # Convert data to DataFrame
            df = pd.DataFrame(data)

            # Save data to CSV
            output_file = f'{sheet_name}_timetable.csv'
            df.to_csv(output_file, index=False)
            print(f"Data for sheet '{sheet_name}' has been saved to {output_file}")

            all_sheets_data[sheet_name] = df

        except Exception as e:
            print(f"Failed to switch to sheet {sheet_name}: {e}")

    # Close the browser
    driver.quit()

    return all_sheets_data


# Example usage
if __name__ == "__main__":
    scrape_timetable(url)
