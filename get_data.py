import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:100.0) Gecko/20100101 Firefox/100.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate',
    'Origin': 'http://sic1.ddnsfree.com:8008',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'http://sic1.ddnsfree.com:8008/avirn/',
    'Upgrade-Insecure-Requests': '1',
    'Sec-GPC': '1',
}

def getData(date: str, type: int):
    types = {1: "Теоретски дел", 2: "Прв практичен дел", 3: "Втор практичен дел"}
    btnNames = {1: "Teorija", 2: "Poligon", 3: "Grad"}

    data = {
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': '/wEPDwUKLTY4NTIxNzE3OA9kFgJmD2QWAgIDD2QWAgIBD2QWBgIDDw8WGB4NRm9udF9PdmVybGluZWgeCUZvbnRfU2l6ZSgqIlN5c3RlbS5XZWIuVUkuV2ViQ29udHJvbHMuRm9udFVuaXQAHgJUUgUBUh4ORm9udF9TdHJpa2VvdXRoHgJUVgUBVh4EXyFTQgKA/AMeDkZvbnRfVW5kZXJsaW5laB4JRm9udF9Cb2xkaB4KRm9udF9OYW1lc2QeC0ZvbnRfSXRhbGljaB4CVEUFAUUeAlRUBQowNi0wNS0yMDIyZGQCDQ8PFgIeBFRleHQFcdCg0JXQl9Cj0JvQotCQ0KLQmCDQntCUINCi0JXQntCg0JXQotCh0JrQmCDQlNCV0Jsg0J7QlCDQktCe0JfQkNCn0JrQmNCe0KIg0JjQodCf0JjQoiDQntCUIDA2LTA1LTIwMjIg0JPQntCU0JjQndCQZGQCDw88KwARAwAPFgQeC18hRGF0YUJvdW5kZx4LXyFJdGVtQ291bnRmZAEQFgAWABYADBQrAABkGAEFG2N0bDAwJE1haW5Db250ZW50JEdyaWRWaWV3MQ88KwAMAQhmZKKxd9ATW59F+RPvtbdjPaUBknGbxmzQNUYARDEFhUza',
        '__VIEWSTATEGENERATOR': 'B16A2D06',
        '__EVENTVALIDATION': '/wEdAAU7XjR9UxS8LaJRXgoaf3/Mc60/zv3NjnmAFaEK8HFwnQGN40Q7hKa+E8RZ/PQXgBPRN8m7t9pinZN1mywcRzNEkqn6Qgh7F8CaQVSKAdKTz2x9FBZuC30R7OgK7XUFZ8eRYRj6qzH1Csr3XTlYbwzL',
        'ctl00$MainContent$textDatumOd': date,
        f'ctl00$MainContent$btn{btnNames[type]}': types[type],
    }

    response = requests.post('http://sic1.ddnsfree.com:8008/avirn/', headers=headers, data=data)
  return response.text

