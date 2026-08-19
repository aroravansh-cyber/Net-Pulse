🌐 NetPulse — Website Connection Monitor

«A lightweight Python-based network monitoring tool for real-time website connectivity and TCP latency monitoring.»

---

🚀 Features

- 🌐 Website / domain input
- 🔍 DNS resolution
- 📍 IP address detection
- 🔐 HTTP / HTTPS detection
- 🔌 Automatic port selection
- 📡 Live TCP connection monitoring
- ⚡ Connection latency measurement
- ⏱️ Connection timeout detection
- 🛑 Press any key to stop monitoring

---

🛠️ Technologies

Python 3
├── Socket Programming
├── DNS Resolution
├── TCP Networking
└── Real-Time Monitoring

---

▶️ Run NetPulse

python website_monitor.py

Enter a website:

Enter website URL: https://google.com

---

💻 NetPulse Terminal

╔═══════════════════════════════════════════════════════════╗
║                 ⚡ NETPULSE v1.0                         ║
║              WEBSITE CONNECTION MONITOR                 ║
╚═══════════════════════════════════════════════════════════╝

┌─[ Network Information ]───────────────────────────────────┐
│                                                           │
│  Website      : google.com                                │
│  IP Address   : 142.250.xxx.xxx                           │
│  Protocol     : HTTPS                                     │
│  Port         : 443                                       │
│                                                           │
└───────────────────────────────────────────────────────────┘

┌─[ Live Connection Monitor ]───────────────────────────────┐
│                                                           │
│  Press any key to exit                                    │
│                                                           │
│  [001]  ✓ Connected     | Latency: 38.21 ms              │
│  [002]  ✓ Connected     | Latency: 41.07 ms              │
│  [003]  ✓ Connected     | Latency: 36.92 ms              │
│  [004]  ✓ Connected     | Latency: 39.45 ms              │
│  [005]  ✓ Connected     | Latency: 42.18 ms              │
│  [006]  ✓ Connected     | Latency: 37.81 ms              │
│  [007]  ✓ Connected     | Latency: 40.26 ms              │
│  [008]  ✓ Connected     | Latency: 43.17 ms              │
│  [009]  ✗ Connection failed                              │
│  [010]  ✓ Connected     | Latency: 39.72 ms              │
│                                                           │
└───────────────────────────────────────────────────────────┘

[+] Monitor stopped.

---

🔎 Understanding the Output

Output| Meaning
"IP Address"| IP address resolved from the domain
"HTTPS"| Website is using HTTPS
"Port 443"| TCP port used for HTTPS
"Connected"| TCP connection was successfully established
"Latency"| Time required to establish the TCP connection
"Connection failed"| TCP connection could not be established
"Timeout"| Connection did not respond within the configured timeout

---

⚙️ How NetPulse Works

              ┌──────────────────┐
              │   Website URL    │
              └────────┬─────────┘
                       ↓
              ┌──────────────────┐
              │ Extract Hostname │
              └────────┬─────────┘
                       ↓
              ┌──────────────────┐
              │  DNS Resolution  │
              └────────┬─────────┘
                       ↓
              ┌──────────────────┐
              │   Get IP Address │
              └────────┬─────────┘
                       ↓
              ┌──────────────────┐
              │ Detect HTTP/HTTPS│
              └────────┬─────────┘
                       ↓
              ┌──────────────────┐
              │ Select Port      │
              │    80 / 443      │
              └────────┬─────────┘
                       ↓
              ┌──────────────────┐
              │ TCP Connection   │
              └────────┬─────────┘
                       ↓
              ┌──────────────────┐
              │ Calculate        │
              │ Latency          │
              └────────┬─────────┘
                       ↓
              ┌──────────────────┐
              │ Display Result   │
              │ Every Second     │
              └──────────────────┘

---

📂 Project Structure

NetPulse/
│
├── website_monitor.py
└── README.md

---

⚠️ Important Note

NetPulse currently performs a TCP connectivity check. It is not an ICMP ping implementation.

Use the tool only on websites and systems you are authorized to test.

---

🔮 Future Improvements

- [ ] ICMP ping support
- [ ] Packet-loss calculation
- [ ] Live latency graph
- [ ] Multiple website monitoring
- [ ] Uptime statistics
- [ ] CSV / JSON logging
- [ ] SSL/TLS certificate monitoring
- [ ] Web dashboard
- [ ] Linux support

---

👨‍💻 Author

Vansh Arora

Cybersecurity Engineering Student

Project: NetPulse
