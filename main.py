from google_osint import start_google_search
from Tor_osint import start_Tor_search

from colorama import Fore, Back, Style

print(Fore.WHITE +'\r\nMultiple search Browser: ' + Fore.CYAN + '''

google            • google-32X/64X • google [vesion (110.0.5481.41) ]
Chrome (web)      • chrome  • web-javascript • Google Chrome 105.0.5195.127 

    add --save how argument in console to save finded links in text file. File will be located in osint.py directory. Example: 
'''+Fore.MAGENTA+"       python3 osint.py --save\r\n")
print (Fore.WHITE + '[1]: google search (google)')
print (Fore.WHITE + '[2]: deep search (tor)\r\n')
Qmode = input(Fore.GREEN + 'Please choose one (To quit, press "Enter") ')
if Qmode == '1':
    start_google_search()
if Qmode == '2' :
    start_Tor_search()