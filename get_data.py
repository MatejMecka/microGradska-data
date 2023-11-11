import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://sic1.ddnsfree.com:8008',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'http://sic1.ddnsfree.com:8008/avirn/',
    'Upgrade-Insecure-Requests': '1',
    'Sec-GPC': '1',
}

def getData(date: str, type: int):
    types = {1: "Теоретски+дел", 2: "Прв+практичен+дел", 3: "Втор+практичен+дел"}
    btnNames = {1: "Teorija", 2: "Poligon", 3: "Grad"}

    data = {
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': '/wEPDwUKLTY4NTIxNzE3OA9kFgJmD2QWAgIDD2QWAgIBD2QWBAIDDw8WCB4CVFQFCjI5LTEwLTIwMjMeAlRWBQFWHgJURQUBRR4CVFIFAVJkZAIPDzwrABEDAA8WBB4LXyFEYXRhQm91bmRnHgtfIUl0ZW1Db3VudGZkARAWABYAFgAMFCsAAGQYAQUbY3RsMDAkTWFpbkNvbnRlbnQkR3JpZFZpZXcxDzwrAAwBCGZkhmTqRnH8vYPtaSZuJB87EXdwqqZSX1OBHwNy0twB5+o=',
        '__VIEWSTATEGENERATOR': '101727CB',
        '__EVENTVALIDATION': '/wEdAAXnvX7REMNBCjdwtuSN+Hx+c60/zv3NjnmAFaEK8HFwnQGN40Q7hKa+E8RZ/PQXgBPRN8m7t9pinZN1mywcRzNEkqn6Qgh7F8CaQVSKAdKTzzlaO0mcabfPqx7h1NTiQphiDK7G0RGUYK7flCUVPBPb',
        'ctl00$MainContent$textDatumOd': date,
        f'ctl00$MainContent$btn{btnNames[type]}': types[type],
    }

    response = requests.post('http://sicrez.ddns.net:8008/avir1/', headers=headers, data=data)
    return response.text

