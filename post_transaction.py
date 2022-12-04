import requests
import json
import datetime
import binascii

from ecdsa import SigningKey
from ecdsa import SECP256k1


def main(
    secret_key_str, sender_pub_key_str, receiver_pub_key_str, amount, description, url
):
    time = datetime.datetime.now().isoformat()

    transaction_unsigned = {
        "time": time,
        "sender": sender_pub_key_str,
        "receiver": receiver_pub_key_str,
        "amount": amount,
        "description": description,
    }

    secret_key = SigningKey.from_string(
        binascii.unhexlify(secret_key_str), curve=SECP256k1
    )
    signature_str = signature(transaction_unsigned, secret_key)

    transaction = {
        "time": time,
        "sender": sender_pub_key_str,
        "receiver": receiver_pub_key_str,
        "amount": amount,
        "description": description,
        "signature": signature_str,
    }

    res = requests.post(url, json.dumps(transaction))

    print(res.json())


def signature(transaction_unsigned, secret_key):
    transaction_json = json.dumps(transaction_unsigned)
    transaction_bytes = bytes(transaction_json, encoding="utf-8")
    signature = secret_key.sign(transaction_bytes)
    signature_str = signature.hex()
    return signature_str


if __name__ == "__main__":
    url = "http://127.0.0.1:8002/transaction_pool/"
    secret_key_str = ""
    sender_pub_key_str = ""
    receiver_pub_key_str = ""
    amount = 222
    description = "test"
    main(
        secret_key_str,
        sender_pub_key_str,
        receiver_pub_key_str,
        amount,
        description,
        url,
    )
