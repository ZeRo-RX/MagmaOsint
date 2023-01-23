from colorama import Fore, Back, Style, init
import sys

def start_Tor_search ():
    init(autoreset=True)
    SaveInFile = "--save" in sys.argv
    print(Fore.MAGENTA + '''
	  █▀▄▀█ █▀▀█ █▀▀▀ █▀▄▀█ █▀▀█   █▀▀█ █▀▀ ░▀░ █▀▀▄ ▀▀█▀▀
	  █░▀░█ █▄▄█ █░▀█ █░▀░█ █▄▄█   █░░█ ▀▀█ ▀█▀ █░░█ ░░█░░
	  ▀░░░▀ ▀░░▀ ▀▀▀▀ ▀░░░▀ ▀░░▀   ▀▀▀▀ ▀▀▀ ▀▀▀ ▀░░▀ ░░▀░░
	                                   Created by LimerBoy
	''' +Fore.YELLOW+"                            some modded by m1n64")
    print(Fore.CYAN+'''
	add --save how argument in console to save finded links in text file. File will be located in osint.py directory. Example: 
	'''+Fore.MAGENTA+"python3 osint.py --save")

    InResults = input(Back.BLACK + Fore.YELLOW + 'results  > ' + Back.RESET + Fore.WHITE)
    query = input(Back.BLACK + Fore.YELLOW + 'Find > ' + Back.RESET + Fore.WHITE)
    results = int(InResults)
    
