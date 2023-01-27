import requests

from multiprocessing.pool import ThreadPool
from torpy.http.requests import tor_requests_session

session = requests.session()
session.proxies = {}
session.proxies['http'] = 'socks5h://localhost:9050'
session.proxies['https'] = 'socks5h://localhost:9050'

with tor_requests_session() as s:  # returns requests.Session() object
    links = ['http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion', 'https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/'] * 2

    with ThreadPool(3) as pool:
        pool.map(s.get, links)