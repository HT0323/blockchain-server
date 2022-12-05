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
    secret_key_str = "595696266b4e7f49fac6e84d95492a39bcb7863297c4ca914c478dcc8ca8aabf"
    sender_pub_key_str = "f70025fda19cf1aa34c5e71b36e1b5f8ea297709d9f22b5dc5bea127a65cff29774d59ae385a98ad02af6ca5a8262772acfdb6d619d33d9c4d4e6ee4cb5f86cf"
    receiver_pub_key_str = "569fbd746ae8ab2998a04d41420a2b6511d91ef47937f7890c07f7ba6dd5697d9cf977e72bf0bd4c6b6b6a45c1f9d22936a7c374835aafdf56ad2ced254d5c50"
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
