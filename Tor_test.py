from requests_tor import RequestsTor

rt = RequestsTor(tor_ports=(9000, 9001, 9002, 9003, 9004), autochange_id=1)

urls = (f'https://habr.com/ru/post/{x}' for x in range(1, 51))
r = rt.get_urls(urls)
print(r[-1].text)