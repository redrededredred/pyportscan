"""
Implements tcp portscanning capabilities.
"""

def handle_ipv4(address: str) -> list:
    """
    Takes either a single IPv4 or a range of IPv4s
    and returns a list contain all addresses to check.
    """
    # Check if range or single ip
    if "/" in address:
        address.split("/")

def handle_port(port: str) -> bool:
    """
    Checks if a given tcp port is valid.
    """
    pass

def check_connection(address: str) -> bool:
    """
    """