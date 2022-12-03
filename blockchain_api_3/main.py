from fastapi import FastAPI
import blockchain
from pydantic import BaseModel


class Transaction(BaseModel):
    time: str
    sender: str
    receiver: str
    amount: int
    description: str
    signature: str


blockchain = blockchain.BlockChain()
app = FastAPI()


# トランザクションプール情報を返却
@app.get("/transaction_pool")
def get_transaction():
    return blockchain.transaction_pool


# チェーン情報を返却
@app.get("/chain")
def get_chain():
    return blockchain.chain


# トランザクションをトランザクションプール情報に追加
@app.post("/transaction_pool")
def post_transaction_pool(transaction: Transaction):
    blockchain.add_transaction_pool(transaction)
    blockchain.broadcast_transaction(transaction)
    return {"message": "Transaction is posted."}


# ブロック生成
@app.get("/create_block/{creator}")
def create_block(creator: str):
    blockchain.create_new_block(creator)
    return {"message": "New Block is Created."}


# トランザクションのブロードキャストの受信
@app.post("/receive_transaction")
def receive_transaction(transaction: Transaction):
    blockchain.add_transaction_pool(transaction)
    return {"message": "Broadcast Transaction is success."}
