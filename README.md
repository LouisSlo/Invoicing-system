# Invoicing System

## Description
The Invoicing System is a fully functional, object-oriented Command Line Interface (CLI) application built in Python. It allows users to create invoices, manage clients, add items with automatic tax calculations, filter items, and securely save the invoice data to JSON files.

This project was designed to demonstrate advanced Python concepts:
* **Object-Oriented Programming (OOP):** Modular architecture with classes (`Client`, `Item`, `Invoice`, `InvoiceManager`).
* **Decorators:** Custom `@log_execution` decorator for logging method calls and execution time.
* **Generators:** Memory-efficient filtering of invoice items (`get_items_above_price`).
* **Lambda Functions:** Used in the `__str__` method of the `Invoice` class to sort items by net price.
* **Regular Expressions (Regex):** Strict validation of the Polish NIP number (must be exactly 10 digits).
* **Exception Handling:** Custom `InvalidNIPError` exception and robust `try-except` blocks to prevent crashes.
* **Context Managers:** Safe file operations utilizing the `with` statement for JSON serialization.
* **Collections & Comprehensions:** Utilizing lists and list comprehensions for dynamic financial calculations.

## Prerequisites
* **Python 3.8+** must be installed on your system.
* No external libraries or dependencies are required (the project strictly uses built-in Python modules such as `re`, `json`, `time`, and `functools`).

## How to Run
To start the application, follow these steps:
1. Extract the project files from the `.zip` archive to a folder of your choice.
2. Open a terminal or command prompt.
3. Navigate to the root directory of the project (where the `main.py` file is located).
4. Run the application using the following command:
   ```bash
   python main.py
   
## Phase 2: Interacting with the Menu
Once the program starts, you will see the INVOICING SYSTEM main menu in your console. You interact with the program by typing a number (from 1 to 6) and pressing Enter.

To fully test all features of the application, follow this recommended workflow:

* Type 1 (Create a new invoice): The system will prompt you for invoice and client details.
 
Important: When asked for the client's NIP, you must enter exactly 10 digits (e.g., 1234567890). If you enter an invalid format, the custom Regex validation will catch it and raise an InvalidNIPError.
  
* Type 2 (Add an item to the invoice): Enter the name of the service/product, its net price (e.g., 150.0), and quantity. You can repeat this step multiple times to add several items to your invoice.
     

* Type 3 (Display the current invoice): View your generated invoice. You will notice that the total net and gross amounts are automatically calculated, and the items are sorted by price (utilizing a lambda function).
                 

* Type 5 (Filter items by minimum price): Test the application's Generator functionality. Enter a minimum price threshold (e.g., 100), and the system will yield and display only the items that cost strictly more than that amount.
            

* Type 4 (Save invoice to JSON): Type a desired file name (e.g., my_invoice.json) and press Enter. The system will serialize your invoice data and safely save it to your local disk using a context manager.
            

* Type 6 (Exit): Safely terminate the application once you are done testing.