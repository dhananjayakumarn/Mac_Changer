import subprocess
from pyfiglet import *
from termcolor import *

Figlet = Figlet(font="slant")
print(Figlet.renderText("MAC--CHANGER"))
cprint(f"\t\t\t\t\t\t\t####|Created By DANNY|####", 'red')

cprint("\n************ \\\\MAC_ADDRESS CHANGER\\\\************\n", 'red')


interface = input("[+] Enter the interface :--")
new_mac = input("[+] Enter the new MAC ADDRESS:--")
print("[+] MAC ADDRESSING CHANGED SUCCESFULLY...")

subprocess.call(f"ifconfig {interface} down",shell=True)
subprocess.call(f"ifconfig {interface} hw ether {new_mac}",shell=True)
subprocess.call(f"ifconfig {interface} up",shell=True)

output = subprocess.check_output(f"ifconfig {interface}",shell=True)


