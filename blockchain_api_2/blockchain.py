import datetime
import requests
import json
import api_list

from ecdsa import VerifyingKey
from ecdsa import SECP256k1
import binascii

REWORD_AMOUNT = 999
# OTHER_API_LIST = api_list.PRD_API_LIST
OTHER_API_LIST = api_list.DEV_API_LIST


class BlockChain(object):
    def __init__(self):
        self.transaction_pool = {"transactions": []}
        self.chain = {"blocks": []}

    # トランザクションプールにトランザクションを追加
    def add_transaction_pool(self, transaction):
        transaction_dict = transaction.dict()
        self.transaction_pool["transactions"].append(transaction_dict)

    # 新たにブロックを作成
    def create_new_block(self, creator):
        # リワードのトランザクションを生成
        reword_transaction_dict = {
            "time": datetime.datetime.now().isoformat(),
            "sender": "Blockchain",
            "receiver": creator,
            "amount": REWORD_AMOUNT,
            "description": "reword",
            "signature": "not need",
        }

        # トランザクションプールからトランザクションを取得してリワードのトランザクションを追加
        transactions = self.transaction_pool["transactions"].copy()
        transactions.append(reword_transaction_dict)

        # ブロック生成
        block = {
            "time": datetime.datetime.now().isoformat(),
            "transactions": transactions,
            "hash": "hash_sample",
            "nonce": 0,
        }

        # 生成したブロックをチェーンに追加してトランザクションプールを初期化
        self.chain["blocks"].append(block)
        self.transaction_pool["transactions"] = []

    # トランザクションが追加された際に他のサーバーに転送
    def broadcast_transaction(self, transaction):
        transaction_dict = transaction.dict()
        for url in OTHER_API_LIST:
            res = requests.post(
                url + "/receive_transaction", json.dumps(transaction_dict)
            )
            print(res.json())

    # チェーンにブロックが追加された際に他のサーバーに転送
    def broadcast_chain(self, chain):
        for url in OTHER_API_LIST:
            res = requests.post(url + "/receive_chain", json.dumps(chain))
            print(res.json())

    # 　　ブロードキャストの際に　chainを更新し、トランザクションプールを初期化
    def replace_chain(self, chain):
        chain_dict = chain.dict()
        self.chain = chain_dict
        self.transaction_pool["transactions"] = []

    # トランザクションの検証
    def verify_transaction(self, transaction):
        public_key = VerifyingKey.from_string(
            binascii.unhexlify(transaction.sender), curve=SECP256k1
        )
        signature = binascii.unhexlify(transaction.signature)

        transaction_unsigned = {
            "time": transaction.time,
            "sender": transaction.sender,
            "receiver": transaction.receiver,
            "amount": transaction.amount,
            "description": transaction.description,
        }

        transaction_unsigned_json = json.dumps(transaction_unsigned)
        transaction_unsigned_bytes = bytes(transaction_unsigned_json, encoding="utf-8")

        return public_key.verify(signature, transaction_unsigned_bytes)
