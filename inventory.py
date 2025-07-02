"""
Compulsory Task - OOP Synthesis
This module functions as a shoe inventory system.

It allows the user to view the stock, restock the lowest item,
capture new shoes and write to a txt file, search the stock,
view the highest stock and put it on sale.
"""
# File was not being recognised
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Import the tabulate module
from tabulate import tabulate

# ========The beginning of the class==========


class Shoe:
    """
    A class to represent and store a shoe.
    """
    def __init__(self, country, code, product, cost, quantity):
        """
        Constructor initializes the attributes of the shoe

        Parameters:
        country (str): The country that the shoe is stocked in.
        code (str): The unique product code.
        product(str): The name of the shoe.
        cost(float): The price of the shoe.
        quantity(int): The amount of product in stock.
        """
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        """
        Returns the cost of the shoe in this method.
        """
        return self.cost

    def get_quantity(self):
        """
        Returns the quantity of the shoes.
        """
        return self.quantity

    def __str__(self):
        """
        Returns a string representation of the class.
        """
        return (
            f"Country: {self.country} \n"
            f"Code: {self.code} \n"
            f"Product: {self.product} \n"
            f"Cost: {self.cost} \n"
            f"Quantity: {self.quantity} \n"
        )

# =============Shoe list===========
# Stores a list of objects of shoes.


shoe_list = []


# ==========Functions outside the class==============
def read_shoes_data():
    """
    This function opens the file inventory.txt and reads the data from
    this file.

    It then create a shoes object with this data and appends
    this object into the shoes list
    """
    try:
        # Open the inventory file in read mode
        with open('inventory.txt', 'r', encoding='utf-8') as file:

            # Skip the first line as it contains headers
            next(file)

            # Iterate through and read each line in the file
            for line in file:

                # Split the line into a list of elements.
                elements = line.strip().split(",")

                # If there are 5 elements append the each element
                # to the list
                if len(elements) == 5:
                    # Each element is associated with the corresponding index
                    country = elements[0]
                    code = elements[1]
                    product = elements[2]
                    cost = float(elements[3])
                    quantity = int(elements[4])

                    # Create and append the shoe object to the shoe list.
                    shoe_list.append(
                        Shoe(country, code, product, cost, quantity)
                    )

    except FileNotFoundError:
        # Print an error if the file is not found.
        print("The file inventory.txt was not found")


def capture_shoes():
    """
    This function allows a user to capture data
    about a shoe and use this data to create a shoe object
    and appends this object inside the shoe list.
    """
    # Continue to loop the input until a valid input is entered
    while True:
        country = input("Please enter the country: \n")

        # Check if the input contains only letters
        if country.replace(" ", "").isalpha():
            break
        print("Please enter letters only.")

    while True:
        code = input("Please enter the product code: \n").strip().upper()

        # Variable to track if the code is unique
        not_unique = False

        # Check if the code is too short
        if len(code) < 8:
            print("This code is too short")
            print("Please enter an 8 character code.")
            not_unique = True

        # Check if the code is too long
        if len(code) > 8:
            print("This code is too long")
            print("Please enter an 8 character code.")
            not_unique = True

        # Check if the code is unique
        for i in shoe_list:
            if i.code == code:
                print("This product code exists. Please enter a unique code")
                not_unique = True

        # Exit the loop if the code is 8 characters and unique
        if not_unique is False:
            break

    while True:
        product = input("Please enter the product: \n")

        # Check if the input is blank
        if not product:
            print("This field cannot be blank.")

            # If the input is blank continue to loop
            continue
        break       # Exit the loop if the input is not blank

    while True:
        try:
            cost = float(input("Please enter the cost: \n"))

            # Check if the input is negative
            if cost < 0:
                print("Please enter a positive number")
                continue        # Continue to loop if input is negative.
            break       # Exit the loop if the input is valid.

        except ValueError:
            # Print an error message if the input is not a number.
            print("Value incorrect. Please enter a number.")

    while True:
        try:
            quantity = int(input("Please enter the quantity: \n"))

            # Check if the input is negative.
            if quantity < 0:
                print("Please enter a positive number")
                continue        # Continue to loop if input is negative.
            break       # Exit the loop if the input is valid.
        except ValueError:
            # Print an error message if the input is not a number.
            print("Please enter a number.")

    # Create the shooe object.
    shoe_capture = Shoe(country, code, product, cost, quantity)

    # Append the shoe to the list.
    shoe_list.append(shoe_capture)


def view_all():
    """
    This function iterates over the shoes list and
    prints the details of the shoes returned from the __str__
    function.

    """
    # Check if there are shoes in the list.
    if len(shoe_list) == 0:
        print("There is no current stock")
        return

    # Tabulate the list and print
    else:
        table = []
        for shoe in shoe_list:
            table.append([
                shoe.country,
                shoe.code,
                shoe.product,
                shoe.cost,
                shoe.quantity
            ])
        # Column headers
        headers = ["Country", "Code", "Product", "Cost", "Quantity"]

        # Generate Table
        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))


def re_stock():
    """
    This function finds the shoe object with the lowest quantity.
    It then given the user the option to restock this item and updates
    the stock count in the list and file.
    """
    # Sort list according to the ascending order of quantity.
    sorted_shoe_list = sorted(shoe_list, key=lambda shoes: shoes.quantity)

    # Print the first object in the list.
    print(f"The shoe with the lowest quantity is {sorted_shoe_list[0]}")

    # Ask the user if they would like to update the quantity.
    response = input(
            "Would you like to update the quantity? Y/N \n"
    ).strip().lower()

    if response == "y":

        while True:
            try:
                # Request the user to enter the new quantity.
                new_quantity = int(input("Please enter new value: \n"))

                if new_quantity < 0:
                    print("Please enter a positive number.")
                    continue
                break
            except ValueError:
                print("Value incorrect. Please enter a number.")

        # Use a variable to track the position of a shoe.
        pos = -1

        # Loop through list to check if there are matching codes.
        for item in shoe_list:

            # Add one to the position after each iteration to track
            # the current index.
            pos = pos + 1
            if item.code == sorted_shoe_list[0].code:
                break       # Exit loop when a code matches

        # When the match is found, update its quantity by adding the new
        # quantity.
        if pos != -1:
            shoe_list[pos].quantity = shoe_list[pos].quantity + new_quantity
            print(shoe_list[pos])

            # Open the file to write the new data.
            with open("inventory.txt", "w", encoding='utf-8') as file:

                # Write the header row to file.
                file.write("Country,Code,Product,Cost,Quantity \n")

                # Write the details of each shoe to the file.
                for shoe in shoe_list:
                    file.write(
                        shoe.country + "," +
                        shoe.code + "," +
                        shoe.product + "," +
                        str(shoe.cost) + "," +
                        str(shoe.quantity) +
                        "\n"
                    )


def search_shoe(shoe_list):
    """
     This function searchs for a shoe from the list
     using the shoe code and returns this object so that it will be printed.
    """
    while True:
        # Request user to input the code.
        shoe_code = input("Please enter the shoe code: \n").strip().lower()

        # Loop through each row in the list and check each code.
        for shoe in shoe_list:

            # If the code matches print the details of the shoe.
            if shoe.code.lower() == shoe_code:
                print("\nShoe details: \n")
                print(shoe)
                return

        # Print message if shoe is not found.
        print("The shoe was not found")

        # Ask the user if they would like to search again.
        re_search = input(
            "Would you like to search again? (Y/N)"
        ).strip().lower()

        # If yes, continue the loop.
        if re_search == "y":
            continue

        # Else stop the loop.
        else:
            menu()
            return


def value_per_item():
    """
    This function calculates the total value for each item.
    This information is then printed in the console for all the shoes.
    """
    # Create an empty table
    value_table = []

    # Loop through the list and multiply the cost to the quantity
    # for each shoe
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity

        # Append each value to the table
        value_table.append([shoe.product, f"R {value}"])

    # Column headers
    headers = ["Product", "Value"]

    # Generate Table
    print(tabulate(value_table, headers=headers, tablefmt="fancy_grid"))


def highest_qty():
    """
    This function determines the product with the highest quantity and
    prints this shoe as being for sale.
    """
    # Sort the shoe list in descending order and print the shoe in the
    # first index.
    sorted_shoe_list = sorted(
        shoe_list,
        key=lambda shoes: shoes.quantity,
        reverse=True
    )

    print(
        f"The shoe with the highest quantity is {sorted_shoe_list[0].product}"
    )

    print("This shoe is on sale")


# ==========Main Menu=============


def menu():
    """
    This function displays the different options to the user.
    It also loops through and calls the functions as needed.
    """
    # Create a variable to store options
    options = [
        ["Capture", "Capture a new shoe"],
        ["View", "View all shoes in stock."],
        ["Restock", "View the item with the lowest quantity and restock"],
        ["Search", "Search for a shoe using the product code"],
        ["Total Value", "Calculate the total value of each item in stock."],
        [
            "Sale",
            "View the product with the highest quantity and mark it on sale"
        ],
        ["Exit", "Exit the inventory system"],
        ]

    headers = ["Option", "Description"]

    print(tabulate(options, headers=headers, tablefmt="fancy_grid"))

    # Initialize the menu variable to an empty string
    menu_var = ""

    # Loop through the menu in the event that there is more than one
    # procedure to be carried out.
    while menu_var == "":

        menu_var = input(
            "\n Please select an option from the menu above: \n"
        ).strip().lower()

        # Loop until a valid input.
        while (
            menu_var != "capture"
            and menu_var != "view"
            and menu_var != "restock"
            and menu_var != "search"
            and menu_var != "total value"
            and menu_var != "sale"
            and menu_var != "exit"
        ):
            print("Invalid input.\n")

            menu_var = input(
                "Please select one of the following:"
                "Capture, View, Restock, Search, Total Value, Sale, Exit:\n"
            ).strip().lower()

        if menu_var == "capture":
            capture_shoes()
            menu()

        elif menu_var == "view":
            view_all()
            menu()

        elif menu_var == "restock":
            re_stock()
            menu()

        elif menu_var == "search":
            search_shoe(shoe_list)
            menu()

        elif menu_var == "total value":
            value_per_item()
            menu()

        elif menu_var == "sale":
            highest_qty()
            menu()

        elif menu_var == "exit":
            print("Thank you for using the Inventory.")

        else:
            menu_var = input(
                "Please select one of the following:"
                "Capture, View, Restock, Search, Total Value, Exit:\n"
            ).strip().lower()


print("\nWelcome to the Inventory \n")
read_shoes_data()
menu()

# References used to understand tables:
# https://pypi.org/project/tabulate/
# https://www.geeksforgeeks.org/python/printing-lists-as-tabular-data-in-python/
# https://www.pythoncentral.io/python-tabulate-creating-beautiful-tables-from-your-data/
