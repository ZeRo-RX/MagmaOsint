from google_osint import start_google_search
from colorama import Fore, Back, Style, init

print ('Multiple search Browser: ')
print ('[1]: google search (google)')
print ('[2]: deap search (tor)')
Qmode = input('Please choose one (To quit, press "ctrl/C")  ')
if Qmode == '1':
    start_google_search()