import gspread
from oauth2client.service_account import ServiceAccountCredentials

def authenticate_google_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name("your-credentials-file.json", scope)
    client = gspread.authorize(credentials)
    return client.open_by_url("https://docs.google.com/spreadsheets/d/1XA76yuFM_4mtkQW__2fryUBMe5EZ6XMWtBHxylhV6k8/edit?gid=837984260")
