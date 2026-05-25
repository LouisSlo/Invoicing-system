import json
from models.invoice import Invoice
from utils.decorators import log_execution

class InvoiceManager:

    @staticmethod
    @log_execution
    def save_to_json(invoice: Invoice, filename: str):
        data = {
            "invoice_number": invoice.invoice_number,
            "client": {
                "name": invoice.client.name,
                "nip": invoice.client.nip,
                "address": invoice.client.address
            },
            "items": [
                {
                    "name": item.name,
                    "net_price": item.net_price,
                    "quantity": item.quantity
                } for item in invoice.items
            ]
        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print(f"Invoice {invoice.invoice_number} saved to {filename}")
