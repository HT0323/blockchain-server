import datetime
import requests
import json
import api_list

REWORD_AMOUNT = 999
OTHER_API_LIST = api_list.API_LIST


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
