import sys
from models.client import Client
from models.invoice import Invoice, Item
from services.invoice_manager import InvoiceManager
from exceptions.custom_errors import InvalidNIPError


def main():
    current_invoice = None

    while True:
        print("\n")
        print("      INVOICING SYSTEM")
        print("\n")
        print("1. Create a new invoice (Client details)")
        print("2. Add an item to the invoice")
        print("3. Display the current invoice")
        print("4. Save invoice to JSON")
        print("5. Filter items by minimum price (Generator Test)")
        print("6. Exit")
        print("\n")

        choice = input("Select an option (1-6): ").strip()

        if choice == '1':
            try:
                invoice_num = input("Enter invoice number (e.g., INV/2026/001): ")
                client_name = input("Enter client name: ")
                client_nip = input("Enter client NIP (10 digits): ")
                client_address = input("Enter client address: ")

                client = Client(client_name, client_nip, client_address)
                current_invoice = Invoice(invoice_num, client)
                print("\n[SUCCESS] Invoice and Client created successfully!")
            except InvalidNIPError as e:
                print(f"\n[ERROR] {e}")

        elif choice == '2':
            if not current_invoice:
                print("\n[WARNING] Please create an invoice first (Option 1).")
                continue

            try:
                item_name = input("Enter item name: ")
                net_price = float(input("Enter net price: "))
                quantity = int(input("Enter quantity: "))

                item = Item(item_name, net_price, quantity)
                current_invoice.add_item(item)
                print(f"\n[SUCCESS] Added '{item_name}' to the invoice!")
            except ValueError:
                print("\n[ERROR] Invalid input! Price must be a number and quantity an integer.")

        elif choice == '3':
            if not current_invoice:
                print("\n[WARNING] No invoice exists yet.")
            else:
                print("\n--- CURRENT INVOICE ---")
                print(current_invoice)

        elif choice == '4':
            if not current_invoice:
                print("\n[WARNING] No invoice to save.")
            else:
                filename = input("Enter filename (e.g., invoice.json): ")
                if not filename.endswith('.json'):
                    filename += '.json'
                InvoiceManager.save_to_json(current_invoice, filename)

        elif choice == '5':
            if not current_invoice or not current_invoice.items:
                print("\n[WARNING] No items in the invoice to filter.")
                continue
            try:
                min_price = float(input("Enter minimum net price to filter: "))
                print(f"\n--- Items with net price > {min_price} PLN ---")

                for item in current_invoice.get_items_above_price(min_price):
                    print(item)
            except ValueError:
                print("\n[ERROR] Invalid price entered.")

        elif choice == '6':
            print("\nExiting the system. Goodbye!")
            sys.exit(0)

        else:
            print("\n[ERROR] Unknown option. Please select a number from 1 to 6.")


if __name__ == "__main__":
    main()