# HEX Log Parser (Device Protocol Analysis)

## 📌 Overview

This project is a Python-based tool for parsing and analyzing HEX logs from device communication protocols.

It simulates real-world scenarios where QA engineers work with low-level device logs, extract packets, and analyze communication between devices.

---

## 🎯 Purpose

The goal of this project is to demonstrate:

* Log analysis skills
* Understanding of low-level communication protocols
* Ability to parse and decode HEX data
* System-level thinking in QA

---

## ⚙️ Features

* Read log files containing HEX data
* Extract HEX sequences from raw logs
* Convert HEX strings into binary data
* Parse packets into:

  * Header
  * Payload
  * Checksum
* Basic packet representation for debugging

---

## 🧩 Project Structure

```
hex-log-parser/
├── data/               # Sample logs
├── parser/             # Core parsing logic
│   ├── reader.py
│   ├── extractor.py
│   ├── decoder.py
│   └── models.py
├── utils/              # Helper functions
├── tests/              # Unit tests
├── main.py             # Entry point
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone repository

```
git clone https://github.com/your-username/hex-log-parser.git
cd hex-log-parser
```

### 2. CLI Usage

```bash
python3 main.py --file data/sample.log
```

---

## 📄 Example Input

```
[INFO] RX: 01 0A FF 23 99
[DEBUG] TX: AA BB CC DD EE
```

---

## 📤 Example Output

```
Packet(header=b'\x01\x0A', payload=b'\xFF\x23', checksum=0x99)
```

---

## 🧠 What I Learned

* Parsing and working with HEX data
* Understanding packet structure (header, payload, checksum)
* Working with logs and extracting meaningful data
* Basics of protocol-level analysis
* Practical Python for system-level tasks

---

## 🔧 Tech Stack

* Python 3
* Regex
* File I/O
* Basic protocol modeling

---

## 📡 Context

This project is inspired by real-world experience working with:

* Device communication logs
* Low-level protocols (e.g., Jeweller, HtS)
* System-level testing and debugging

---

## 🚧 Future Improvements

* Add protocol-specific decoding (commands, types)
* Implement checksum validation
* CLI support for custom log files
* Visualization of packet flow
* Integration with network simulators

---

## 👨‍💻 Author

Oleksii Leontiev
Kyiv, Ukraine

---

