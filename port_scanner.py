import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(target, port, timeout=1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((target, port))

            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except OSError:
                    service = "unknown"

                return port, service

    except socket.gaierror:
        print("Invalid hostname or IP address.")
        return None
    except Exception:
        return None

    return None


def scan_target(target, start_port, end_port, threads=100):
    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

    open_ports = []

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [
            executor.submit(scan_port, target, port)
            for port in range(start_port, end_port + 1)
        ]

        for future in futures:
            result = future.result()
            if result:
                open_ports.append(result)
                port, service = result
                print(f"[OPEN] Port {port} ({service})")

    if not open_ports:
        print("No open ports found.")

    return open_ports


def main():
    print("Python Port Scanner")
    print("-------------------")

    target = input("Enter target IP or hostname: ").strip()
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    scan_target(target, start_port, end_port)


if __name__ == "__main__":
    main()