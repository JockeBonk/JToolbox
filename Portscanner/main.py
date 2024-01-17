"""
This is a basic portscanner
"""

import socket
import concurrent.futures

target = input("Enter a target IP: ")
start_port = 1
end_port = 1000

def port_scan(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            return port
        sock.close()
    except:
        pass
    return None

def scan_ports(target, start_port, end_port):
    open_ports = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        port_list = range(start_port, end_port +1)
        results = {executor.submit(port_scan, target, port): port for port in port_list}
        for future in concurrent.futures.as_completed(results):
            port = results[future]
            if future.result():
                open_ports.append(port)
                print(f"Found open port: {port}")
    return open_ports


print(f"Scanning ports {start_port}-{end_port} on {target}...")

open_ports = scan_ports(target, start_port, end_port)

if open_ports:
    print("All open ports:")
    for port in open_ports:
        print(port)
else:
    print("No open ports found :(")
