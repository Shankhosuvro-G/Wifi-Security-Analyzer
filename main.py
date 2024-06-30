import subprocess
import re

def analyze_wifi_security():
   
    command_output = subprocess.run(["netsh", "wlan", "show", "interfaces"], capture_output=True, text=True).stdout
    security_type_search = re.search(r'Authentication\s+:\s+(\w+)', command_output)
    ssid_search = re.search(r'SSID\s+:\s+(.+)', command_output)
    if security_type_search and ssid_search:
        security_type = security_type_search.group(1)
        ssid=ssid_search.group(1)
        print(f"Network detected with ssid {ssid} and is set to passive mode.")
        print("Determining Wireless Security Protocol......")
        if security_type in ["WPA2", "WPA3"]:
            return f"The network with ssid {ssid} is secured with {security_type}."
        elif security_type == "WEP":
            return f"The network with ssid {ssid} is secured with WEP (not recommended due to security vulnerabilities)."
        elif security_type == "Open":
            return f"The network with ssid {ssid} has no security (Open network)."
        else:
            return "The network security type is not recognized."
    else:
        return "Could not determine the network security type."

if __name__== "__main__":
    print("Scanning connected network......")
    print(analyze_wifi_security())
    print("The operation is successful.")




