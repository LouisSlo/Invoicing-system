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