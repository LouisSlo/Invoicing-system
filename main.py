from models.client import Client
from models.invoice import Invoice, Item
from services.invoice_manager import InvoiceManager


def main():
    try:
        # Create a client
        my_client = Client("Tech Solutions Sp. z o.o.", "1234567890", "Warsaw, Marszałkowska 1")

        # Create an invoice
        my_invoice = Invoice("INV/2026/001", my_client)

        # Add items
        my_invoice.add_item(Item("Software License", 1000.0, 1))
        my_invoice.add_item(Item("Consulting Hours", 250.0, 4))

        # Display invoice
        print(my_invoice)

        # Save to file
        InvoiceManager.save_to_json(my_invoice, "invoice.json")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()