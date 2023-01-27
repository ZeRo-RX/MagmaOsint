from ast import Or
from requests_tor import RequestsTor

# If you use the Tor browser
rt = RequestsTor()
Or
# If you use the Tor
rt = RequestsTor(tor_ports=(9050,), tor_cport=9050)

url = ['http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion']
r = rt.get_urls(url)
print(r[-1].text)