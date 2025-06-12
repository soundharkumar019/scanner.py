import socket
import sys
from datetime import datetime

def scan_ports(target, start_port=1, end_port=1024):
    print(f"\nScanning target: {target}")
    print(f"Scanning ports: {start_port} to {end_port}")
    print("-" * 40)
    start_time = datetime.now()

    try:
        for port in range(start_port, end_port + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port}: OPEN")
            s.close()

    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
        sys.exit()
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("Could not connect to server.")
        sys.exit()

    end_time = datetime.now()
    total_time = end_time - start_time
    print("-" * 40)
    print(f"Scan completed in: {total_time}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scanner.py <target-ip>")
        sys.exit()

    target_ip = sys.argv[1]
    scan_ports(target_ip)
