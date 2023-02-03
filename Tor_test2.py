from stem import Signal
from stem.control import Controller
from requests import get
from fake_useragent import UserAgent
from time import sleep


def new_tor_id():
  with Controller.from_port(port=9051) as controller:
    controller.authenticate(password="your Tor password")
    controller.signal(Signal.NEWNYM)

  
def test_creation_of_new_identity(url: str):
    tor_proxy = {
      "http": "socks5h://127.0.0.1:9050",
      "https": "socks5h://127.0.0.1:9050"
    }
    headers = {
      "User-Agent": UserAgent().random
    }
    resp = get(url, headers=headers, proxies=tor_proxy)
    return resp
 

if __name__ == "__main__":
  for _ in range(10):
    resp = test_creation_of_new_identity("http://httpbin.org/ip")
    print(resp.text)
    new_tor_id()
    # need to wait at least 5 seconds before generating new exit IP
    sleep(5)