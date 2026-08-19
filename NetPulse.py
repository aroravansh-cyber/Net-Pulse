import socket
import time
import os
import msvcrt
from urllib.parse import urlparse

print("=" * 55)
print("          WEBSITE CONNECTION MONITOR")
print("=" * 55)

url = input("Enter website URL: ").strip()

if not url.startswith(("http://", "https://")):
    url = "https://" + url

parsed_url = urlparse(url)
hostname = parsed_url.hostname

if not hostname:
    print("Invalid website URL.")
    exit()

try:
    ip = socket.gethostbyname(hostname)

    print("\n--- Network Information ---")
    print(f"Website    : {hostname}")
    print(f"IP Address: {ip}")
    print(f"Protocol   : {parsed_url.scheme.upper()}")

    if parsed_url.scheme == "https":
        port = 443
    else:
        port = 80

    print(f"Port       : {port}")

except socket.gaierror:
    print("Could not resolve the hostname.")
    exit()

print("\n" + "=" * 55)
print("LIVE CONNECTION MONITOR")
print("Press any key to exit")
print("=" * 55)

count = 1

while True:

    if msvcrt.kbhit():
        msvcrt.getch()
        print("\n\nMonitor stopped.")
        break

    start = time.time()

    try:
        sock = socket.create_connection(
            (hostname, port),
            timeout=3
        )
        sock.close()

        end = time.time()
        latency = round((end - start) * 1000, 2)

        print(
            f"[{count:03}] "
            f"Connected | "
            f"Latency: {latency} ms"
        )

    except socket.timeout:
        print(
            f"[{count:03}] "
            f" Timeout"
        )

    except OSError:
        print(
            f"[{count:03}] "
            f" Connection failed"
        )

    count += 1
    time.sleep(1)
