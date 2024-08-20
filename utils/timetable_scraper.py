from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import FirefoxDriverManager
import pandas as pd
import time


def scrape_timetable(url):
    """
    Scrape the timetable data from Google Sheets using Selenium.
    """
    # Set up the Chrome driver (you can use any other browser)
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')  # Run in headless mode (no GUI)
    driver = webdriver.Firefox(service=Service(FirefoxDriverManager().install()), options=options)

    # Navigate to the Google Sheets URL
    driver.get(url)

    # Wait for the sheet to load (adjust the sleep time as needed)
    time.sleep(5)  # Wait for the sheet to load completely

    # Find the table content (adjust selectors based on the table structure)
    table = driver.find_element_by_xpath('//table[@id="timetable"]')

    # Extract the data into a Pandas DataFrame (adjust based on the structure of your sheet)
    rows = table.find_elements_by_tag_name('tr')
    timetable_data = []
    for row in rows:
        cols = row.find_elements_by_tag_name('td')
        cols = [col.text for col in cols]
        timetable_data.append(cols)

    # Convert to a Pandas DataFrame
    df = pd.DataFrame(timetable_data)

    # Save the DataFrame as a CSV (one for each day, e.g., 'timetable_thursday.csv')
    df.to_csv('data/timetable_thursday.csv', index=False)

    # Close the browser
    driver.quit()

    return df
