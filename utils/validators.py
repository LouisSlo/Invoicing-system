import re
from exceptions.custom_errors import InvalidNIPError

def validate_nip(nip: str) -> str:
    """
    Validates the Polish NIP number using regular expressions.
    Requirements: Exactly 10 digits.
    """
    clean_nip = nip.replace("-", "").strip()
    nip_pattern = r"^\d{10}$"

    if not re.match(nip_pattern, clean_nip):
        raise InvalidNIPError(nip)

    return clean_nip