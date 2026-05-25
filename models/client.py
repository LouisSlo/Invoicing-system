from pyclbr import Class

from utils.validators import validate_nip

Class Client:
def __init__(self, name: str, nip: str, adress: str):
    self.name = name
    self.nip = validate_nip(nip)
    self.adress = adress

    def __str__(self):
        return f"{self.name} (NIP: {self.nip}, Adres: {self.address})"


