from flask import Flask, request
from blockchain import Blockchain
from utils import compute_hash
import json

app = Flask(__name__)

blockchain = Blockchain()
transactions = ["A", "B"]


@app.route("/blockchain", methods=['GET'])
def get_blockchain():
    return json.dumps({"length": len(blockchain.chain)})


@app.route("/blockchain/add_block", methods=['GET'])
def add_block():
    blockchain.create_new_block(transactions)
    block = blockchain.get_last_block()
    return json.dumps({"timestamp": block.timestamp, "previous_hash": block.previous_block_hash,
                       "merkle_root": block.merkle_root})


app.run(debug=True, port=5000)
