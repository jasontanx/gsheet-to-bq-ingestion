
import gspread
from google.oauth2 import service_account

from transform import transform


'''
Reference Sources:

https://developers.google.com/identity/protocols/oauth2/service-account#python 
https://developers.google.com/sheets/api/quickstart/python 

'''
def extract_data():
    SERVICE_ACCOUNT_FILE = 'secret_key.json' # cred to allow that access
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets'] # asking for access to the scope
    credentials = service_account.Credentials.from_service_account_file( # creates actual credentials
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    file = gspread.authorize(credentials)
    workbook = file.open("salaries_ethnicity_sex")
    sheet = workbook.sheet1

    data = sheet.get_all_values() # read in the sheet as a list
    headers = data.pop(0)
    transform(headers)
