import datetime

REWORD_AMOUNT = 999


class BlockChain(object):
    def __init__(self):
        self.transaction_pool = {"transactions": []}
        self.chain = {"blocks": []}

    def add_transaction_pool(self, transaction):
        transaction_dict = transaction.dict()
        self.transaction_pool["transactions"].append(transaction_dict)

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
