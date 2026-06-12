import socket

print("=" * 40)
print("NETWORK PORT SCANNER")
print("=" * 40)

target = input("Enter Target IP: ")

open_ports = []

print(f"\nScanning {target}...\n")

for port in range(1, 9000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")
        open_ports.append(port)

    s.close()

print("\nScan Completed")
print("-" * 40)
print("Open Ports:", open_ports)
print("Total Open Ports:", len(open_ports))
