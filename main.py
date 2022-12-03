from fastapi import FastAPI
import blockchain

blockchain = blockchain.BlockChain()
app = FastAPI()


# トランザクションプール情報を返却
@app.get("/transaction_pool")
def get_transaction():
    return blockchain.transaction_pool


# チェーン情報を返却
@app.get("/chain")
def get_chain():
    pass


# トランザクションをトランザクションプール情報に追加
@app.post("/transaction_pool")
def post_transaction_pool():
    pass


# ブロック生成
@app.get("/create_block")
def create_block():
    pass
