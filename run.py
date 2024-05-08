# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials

# Lists the APIs that the programme should access in order to run
# Not changed - contant so written in capitals
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("love_sandwiches")

# #Calls sales tab from the worksheet
# sales = SHEET.worksheet("sales")

# #Built-in function get_all_values collects all of the data from that tab in the worksheet
# data = sales.get_all_values()

# print(data)

def get_sales_data():
    """
    Function to get sales figures input from user
    """
    print("Please enter sales data from the last market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")#\n added to create space between instructions and place to enter data

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")

#Call the function to run
get_sales_data()