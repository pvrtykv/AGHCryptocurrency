from flask import Flask, request
from blockchain import Blockchain
from utils import compute_hash
import json

app = Flask(__name__)

blockchain = Blockchain()
transactions = ["A", "B"]


@app.route("/blockchain/show_chain", methods=['GET'])
def get_blockchain():
    chain = []
    for block in blockchain.chain:
        chain.append(block.__dict__)
    return json.dumps({"chain": chain,
                            "length": len(blockchain.chain)})


@app.route("/blockchain/add_transaction", methods=['GET'])
def add_transaction():
    blockchain.add_new_transaction(transactions[0])
    return transactions[0]


@app.route("/blockchain/mine_block", methods=['GET'])
def add_block():
    if blockchain.mine() is False:
        return "There is no transactions to put in the block!"
    block = blockchain.get_last_block()
    return json.dumps({"timestamp": block.timestamp, "previous_hash": block.previous_block_hash,
                       "merkle_root": block.merkle_root})


app.run(debug=True, port=5000)
