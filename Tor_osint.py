from Tor_osint_Ahmia import Ahmia
from Tor_osint_Grams import Grams
from Tor_osint_TORCH import TORCH
from Tor_osint_Devil_Search import Devil_Search
from Tor_osint_Search_Demon import Search_Demon

from colorama import Fore, Back, Style, init
import torpy
import requests
import requests_tor
import sys

def start_Tor_search ():
    init(autoreset=True)
    SaveInFile = "--save" in sys.argv
    print(Fore.MAGENTA + '''
	  █▀▄▀█ █▀▀█ █▀▀▀ █▀▄▀█ █▀▀█   █▀▀█ █▀▀ ░▀░ █▀▀▄ ▀▀█▀▀    ▀▀█▀▀ █▀▀█ █▀▀▀▄
	  █░▀░█ █▄▄█ █░▀█ █░▀░█ █▄▄█   █░░█ ▀▀█ ▀█▀ █░░█ ░░█░░ ▀▀ ░░█░░ █░░█ █▀▀▀▄ 
	  ▀░░░▀ ▀░░▀ ▀▀▀▀ ▀░░░▀ ▀░░▀   ▀▀▀▀ ▀▀▀ ▀▀▀ ▀░░▀ ░░▀░░    ░░▀░░ ▀▀▀▀ ▀	 ▀
	                                   Created by LimerBoy
	''' +Fore.YELLOW+"                            some modded by m1n64")

    print(Fore.CYAN + '''
	add --save how argument in console to save finded links in text file. File will be located in osint.py directory. Example: 
	'''+Fore.GREEN + "python3 osint.py --save\r\n")
    print (Back.BLACK + Fore.YELLOW + 'select Your Browser  : ' + Back.RESET)
    print (Fore.MAGENTA +'[1]: Ahmia')
    print (Fore.MAGENTA +'[2]: Devil search')
    print (Fore.MAGENTA +'[3]: Grams')
    print (Fore.MAGENTA +'[4]: TORCH')
    print (Fore.MAGENTA +'[5]: Search Demon' + Back.RESET + Fore.WHITE)
    SetBrowser = input(Fore.WHITE + 'Please choose one (To quit, press "Enter") ')

    if SetBrowser == '1' : 
        Ahmia()

    if SetBrowser == '2' :
        Devil_Search()

    if SetBrowser == '3' :
        Grams()

    if SetBrowser == '4' :
        TORCH()

    if SetBrowser == '5' :
        Search_Demon()

