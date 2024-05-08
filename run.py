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

# ------ TEST IF THE API IS WORKING AND DATA PASSING FROM SHEET ------ #
# # Calls sales tab from the worksheet
# sales = SHEET.worksheet("sales")

# # Built-in function get_all_values collects all of the data from that tab in the worksheet
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
    # print(f"The data provided is {data_str}") #print statement only used to check that input feature working

    # split() method returns the broken up values as a list instead of one long string
    # each object is defined by the "," parameter provided in the split() function
    sales_data = data_str.split(",")
    # print(sales_data) #print statement only used to check that string split is working

    # call validate_data() within the get_sales_data function
    validate_data(sales_data) #sales_data is the data that we want to check


def validate_data(values):
    """
    Inside the try, converts all tring values into integers.
    Raises ValueError if strings cannot be converted into int, 
    or if there aren't exactly 6 values.
    """
    try:
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")


    # print(values) #print statement used to check if values printing from 
    # within the validate_data function instead of 

#Call the function to run
get_sales_data()