from models.client import Client


class Item:
    def __init__(self, name: str, net_price: float, quantity: int = 1, tax_rate: float = 0.23):
        self.name = name
        self.net_price = net_price
        self.quantity = quantity
        self.tax_rate = tax_rate

    @property
    def gross_price(self) -> float:
        return self.net_price * (1 + self.tax_rate)

    @property
    def total_net(self) -> float:
        return self.net_price * self.quantity

    @property
    def total_gross(self) -> float:
        return self.gross_price * self.quantity

    def __str__(self):
        return (f"{self.name} | Quantity: {self.quantity} | "
                f"Net price: {self.net_price:.2f} PLN | "
                f"Total gross: {self.total_gross:.2f} PLN")


class Invoice:
    def __init__(self, invoice_number: str, client: Client):
        self.invoice_number = invoice_number
        self.client = client
        self.items = []  # Collection: list to store invoice items

    def add_item(self, item: Item):
        """Adds a new item to the invoice."""
        self.items.append(item)

    @property
    def total_net_amount(self) -> float:
        """Calculates total net amount of the invoice using list comprehension."""
        return sum([item.total_net for item in self.items])

    @property
    def total_gross_amount(self) -> float:
        """Calculates total gross amount of the invoice."""
        return sum([item.total_gross for item in self.items])

    def __str__(self):
        items_str = "\n".join([str(item) for item in self.items])
        return (f"Invoice Number: {self.invoice_number}\n"
                f"Client: {self.client.name}\n"
                f"Items:\n{items_str}\n"
                f"Total Net: {self.total_net_amount:.2f} PLN\n"
                f"Total Gross: {self.total_gross_amount:.2f} PLN")