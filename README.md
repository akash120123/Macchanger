# 🔧 MAC Changer, My First Dive into Network Tweaking!

A while ago, I got curious about how MAC addresses work and wondered if I could change mine. 

It's simple, to the point, and does exactly what I needed: changes your MAC address from the terminal using Python.

---

## 📌 Features

- 🔄 Changes your MAC address quickly via terminal
- 🔍 Verifies if the MAC address was successfully updated
- 🧰 Uses basic Python libraries: `subprocess`, `optparse`, and `re`

---
## 🛠 OS
Its is supported in Linux 

## 🛠 How to Use

1. **Clone the script** or copy the Python file.

2. **Run the command** below with root privileges:

   ```bash
   sudo python3 mac_changer.py -i <interface> -m <new_mac>
