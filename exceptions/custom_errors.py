class InvalidNIPError(Exception):
    def __init__(self, nip, message="NIP must consist of exactly 10 digits"):
        self.nip = nip
        self.message = f"{message}: '{self.nip}'"
        super().__init__(self.message)