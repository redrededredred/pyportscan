"""
Implements tcp portscanning capabilities.
"""
import socket
import ipaddress

def check_multiple_connections(address: str, port: int) -> list:
    """
    Takes an ipv4 address range + port and tries 
    establishing a connection for every address.
    Prints successes to stdout.

    returns a list of connectable addresses.
    """
    try:
        ipaddress.IPv4Network(address)
    except (ipaddress.AddressValueError, ipaddress.NetmaskValueError, ValueError):
        print("[!] - Invalid IPv4 or Netmask")
        return []
    
    online: list = []

    for ip in ipaddress.IPv4Network(address).hosts():
        if check_connection(str(ip), port):
            online.append(ip)
            print("[+] - Found: ", str(ip))

    return online

def check_connection(address: str, port: int) -> bool:
    """
    Takes an ipv4 address + port and tries 
    establishing a connection.

    returns True if a connection is possible and False otherwise.
    """

    # Check if port and ip are valid
    try:
        ipaddress.IPv4Address(address)
    except ipaddress.AddressValueError:
        print("[!] - Invalid IPv4")
        return False

    if port < 0 or port > 65535:
        print("[!] - Invalid Port")
        return False


    sock: socket.socket = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
    sock.settimeout(0.1)    # assumes no connection is possible after 100ms
    try:
        sock.connect((address, port))
        sock.close()
        return True
    except (ConnectionError, TimeoutError):
        return False
