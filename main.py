from fastapi import FastAPI

app = FastAPI()


# トランザクションプール情報を返却
@app.get("/transaction_pool")
def get_transaction():
    pass


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
