# HEX Log Parser (Protocol-Aware Analysis Tool)

## 🚀 Overview

This project is a Python-based tool for parsing and analyzing HEX logs from device and network communication.

Unlike a simple HEX parser, this tool performs **protocol-aware decoding**, transforming raw binary data into structured, human-readable information.

It simulates real-world scenarios where QA engineers and system engineers analyze low-level logs to debug device behavior and network interactions.

---

## 🎯 Purpose

The goal of this project is to demonstrate:

* Log analysis and debugging skills
* Understanding of protocol-level communication
* Ability to transform raw HEX into structured data
* System-level thinking in QA and backend testing
* Building reusable developer tools

---

## ⚙️ Features

* Read and process log files containing HEX data
* Extract HEX sequences from mixed log formats
* Convert HEX → raw bytes
* **Protocol detection and decoding**

  * HTTP (requests & responses)
  * Redis (RESP protocol)
* Graceful error handling (invalid HEX, corrupted data)
* CLI interface for flexible usage
* JSON output for integration and analysis

---

## 🧠 Supported Protocols

### 🌐 HTTP

* Detects request/response
* Parses:

  * Method / Path / Version
  * Headers
  * Body

### ⚡ Redis (RESP)

* Parses:

  * Arrays
  * Bulk strings
  * Commands (GET, SET, etc.)

---

## 🏗️ Project Structure

```
hex-log-parser/
├── parser/
│   ├── reader.py
│   ├── extractor.py
│   ├── decoder.py        # Protocol dispatcher
│   ├── models.py
│   ├── protocols/
│   │   ├── http.py
│   │   ├── redis.py
│   │   └── mqtt.py
├── utils/
├── tests/
├── main.py
└── README.md
```

---

## 🖥️ CLI Usage

```bash
python3 main.py --file data/sample.log
```

---

## 📥 Example Input (HEX log)

```
[INFO] RX: 47 45 54 20 2F 20 48 54 54 50 2F 31 2E 31 0D 0A
48 6F 73 74 3A 20 65 78 61 6D 70 6C 65 2E 63 6F 6D 0D 0A
0D 0A
```

---

## 📤 Example Output

```json
{
  "protocol": "HTTP",
  "type": "request",
  "method": "GET",
  "path": "/",
  "headers": {
    "Host": "example.com"
  }
}
```

---

## 🧪 Use Cases

* Debugging device ↔ server communication
* Analyzing protocol-level logs
* QA automation tooling
* Reverse engineering simple protocols
* Learning networking fundamentals

---

## 📚 What I Learned

* Working with raw bytes and HEX data
* Protocol detection and decoding strategies
* Designing modular and extensible parsers
* Handling real-world noisy logs
* Building CLI-based developer tools

---

## 🛠️ Tech Stack

* Python 3
* argparse (CLI)
* JSON
* File I/O
* Protocol parsing

---

## 🔮 Future Improvements

* Add MQTT decoder (IoT focus)
* Implement plugin-based protocol registry
* Add packet validation (checksum, length)
* Integrate with TCP traffic simulator
* Export results to structured formats (JSON/CSV files)

---

## 🌍 Context

This project is inspired by real-world experience with:

* Device communication logs
* Low-level protocols (Jeweller, Fibra, HtS)
* System-level QA and debugging

---

## 👤 Author

Oleksii Leontiev
Kyiv, Ukraine
