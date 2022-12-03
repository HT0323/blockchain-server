import requests
import json
import datetime


def main():
    time = datetime.datetime.now().isoformat()

    transaction = {
        "time": time,
        "sender": "Yamada",
        "receiver": "Sato",
        "amount": 999,
        "description": "text",
        "signature": "sample",
    }

    url = "http://127.0.0.1:8000/transaction_pool/"
    res = requests.post(url, json.dumps(transaction))

    print(res.json())


if __name__ == "__main__":
    main()
