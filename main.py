"""
CLI for pyportscan
"""
import scanner

def cli():
    print("*** Pyportscan ***")
    while True:
        print()
        address: str = input("Enter IPv4 or IPv4 Range to scan (e.g. 8.8.8.8 or 1.1.1.1/24): ")
        port: int = int(input("Enter Port to scan (e.g. 80 or 21): "))
        if "/" in address:
            print(str(scanner.check_multiple_connections(address, port)))
        else:
            if scanner.check_connection(address, port):
                print(f"Port {port} open on {address}")
            else:
                print("No connection possible")
def main() -> None:
    cli()

if __name__ == "__main__":
    main()