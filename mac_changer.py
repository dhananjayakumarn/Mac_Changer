import subprocess

interface = input("[+] Enter the interface :--")
new_mac = input("[+] Enter the new MAC ADDRESS:--")
print("[+] MAC ADDRESSING CHANGED SUCCESFULLY...")

subprocess.call(f"ifconfig {interface} down",shell=True)
subprocess.call(f"ifconfig {interface} hw ether {new_mac}",shell=True)
subprocess.call(f"ifconfig {interface} up",shell=True)

output = subprocess.check_output(f"ifconfig {interface}",shell=True)


