# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    Function to get sales figures input from user.
    Run a while loop to collect a valid string of data from the user 
    via the terminal, which must be a string of 6 numbers separated
    by commas. The loop will repeatedly request data, until it is valid.
    """
    while True: #loop to run same code every time an error is raised 
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
        # if statement to close while loop --- while True, it keeps 
        if validate_data(sales_data): #sales_data is the data that we want to check
            print("Data is valid!")
            break

    return sales_data #important! Calls sales_data into the RAM to be used in next steps

def validate_data(values):
    """
    Inside the try, converts all tring values into integers.
    Raises ValueError if strings cannot be converted into int, 
    or if there aren't exactly 6 values.
    """
    try:
        [int(value) for value in values] #converts string number values into int
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False #if error is raised, returns False
    
    return True #if function runs without any errors, then returns True 


    # print(values) #print statement used to check if values printing from 
    # within the validate_data function instead of 

# calls the function to run
# define 'data' variable as the returned results of the get_sales_data() function

def update_worksheet(data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")

# def update_sales_worksheet(data): # data is information to insert
#     """
#     Update sales worksheet, add new row with the list data provided.
#     """
#     # message to give user some feedback in the terminal while program runs
#     # also highlights the point in which code has got to when identifying bugs
#     print("Updating sales worksheet...\n")

#     # access sales sheet so we can add data to it
#     sales_worksheet = SHEET.worksheet("sales")
#     # adds a new row to the worksheet using built-in append_row() function
#     sales_worksheet.append_row(data)
#     print("Sales worksheet updated successfully.\n")

# sales_row only referred to in the calculate_surplus_data function. Didn't already exist
def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.

    The surplus is defined as the sales figure subtracted from the stock:
    - Postive surplus indicates waste.
    - Negative surplus indicates extra stock made when stock was sold out.
    """
    print("Calculating surplus data...\n")
    # gets all data in the stock worksheet
    stock = SHEET.worksheet("stock").get_all_values()
    # pprint(stock) # prettyprint lays out print statement in more readable format
    stock_row = stock[-1]
    # print(f"stock row: {stock_row}") - #returns a list of strings from worksheet
    # print(f"sales row: {sales_row}")


    surplus_data = [] # defines the list name to add surplus data to
    # iterates through each object in the list taking an item 'stock' from stock_row
    # and sales from sales_row.
    for stock, sales in zip(stock_row, sales_row):
        # defines surplus as stock value minus sales value
        surplus = int(stock) - sales
        surplus_data.append(surplus) # adds each surplus value to the surplus_data list

    #print(surplus_data) # print used to check working functionality
    return surplus_data # send surplus_data list to the RAM for future use

# def update_surplus_worksheet(data): # data is information to insert
#     """
#     Update surplus worksheet, add new row with the list data provided.
#     """
#     # message to give user some feedback in the terminal while program runs
#     # also highlights the point in which code has got to when identifying bugs
#     print("Updating surplus worksheet...\n")

#     # access sales sheet so we can add data to it
#     surplus_worksheet = SHEET.worksheet("surplus")
#     # adds a new row to the worksheet using built-in append_row() function
#     surplus_worksheet.append_row(data)
#     print("Surplus worksheet updated successfully.\n")

def get_last_5_entries_sales():
    """
    Collects columns of data from sales worksheet, collecting
    the last 5 entries for each sandwich and returns the data
    as a list of lists.
    """
    sales = SHEET.worksheet("sales")

    columns = [] #defines the list for the results to be added to
    # iterates through each column (range identifies columns to get data from)
    # ** --- Index for rows / columns starts at '1' and NOT '0' --- **
    for ind in range(1, 7): 
        column = sales.col_values(ind) # runs col_values() method for each index
        columns.append(column[-5:]) # '[-5]' splits off last 5 values from each column

    return columns


# function to hold all main funtions and call them at appropriate time
def main():
    """
    Run all program functions
    """
    data = get_sales_data()
    # creates a list called sales_data by appending an int for each object in the data string
    sales_data = [int(num) for num in data]

    # calls update_sales_worksheet() function and passes it the sales_data list that
    # you want to insert
    # REPLACED WITH SINGLE FUNCTION BELOW # update_sales_worksheet(sales_data)
    update_worksheet(sales_data, "sales")

    # calls calculate_surplus_data() function and passes it the sales_data
    new_surplus_data = calculate_surplus_data(sales_data)

    # calls update_surplus_worksheet() function and passes it the new_surplus_data list 
    # that you want to insert
    # REPLACED WITH SINGLE FUNCTION BELOW #update_surplus_worksheet(new_surplus_data)
    update_worksheet(new_surplus_data, "surplus")


# first message you see before any functionality
print("Welcome to Love Sandwiches Data Automation!\n")
# main()
sales_columns = get_last_5_entries_sales() # function turned into a variable sales_columns

