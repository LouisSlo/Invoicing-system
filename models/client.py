from utils.validators import validate_nip

class Client:
    def __init__(self, name: str, nip: str, address: str):
        self.name = name
        self.nip = validate_nip(nip)
        self.address = address  # Ensure this line is present!

    def __str__(self):
        return f"{self.name} (NIP: {self.nip}, Address: {self.address})"