# WiFi Security Analyzer

## Overview
This script analyzes the security configuration of the currently connected WiFi network using `netsh` command-line utility on Windows.

## Features
- Detects the SSID and frequency (2.4GHz or 5GHz) of the connected WiFi network.
- Determines the security protocol (WPA2, WPA3, WEP, Open) of the network.
- Prints information about the network's security status.

## Requirements
- Python 3.x
- Windows operating system (due to the use of `netsh` command)

## Usage
1. Ensure Python 3.x is installed on your system.
2. Run the script using `python wifi_security_analyzer.py`.
3. The script will output the security status of the currently connected WiFi network.

## Example Output
![image](https://github.com/Shankhosuvro-G/Wifi-Security-Analyzer/assets/98182979/285d33de-392e-48c9-b062-dbe9a853af37)


## Notes
- Ensure your WiFi adapter is connected and active to get accurate results.
- This script is designed for use on Windows and may not work on other operating systems without modification.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

