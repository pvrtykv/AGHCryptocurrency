from flask import Flask, request
from blockchain import Blockchain
from transaction import Transaction
from utils import compute_hash
import json

transaction1 = Transaction("Jan", "Andrzej", 400)


app = Flask(__name__)

blockchain = Blockchain()


@app.route("/blockchain/show_chain", methods=['GET'])
def get_blockchain():
    chain = []
    for block in blockchain.chain:
        block_data = json.dumps({"block_header": {
            "timestamp": block.block_header.timestamp,
            "previous_block_hash": block.block_header.previous_block_hash,
            "merkle_root": block.block_header.merkle_root
        }
        })
        chain.append(block_data)
    return json.dumps({"chain": chain,
                        "length": len(blockchain.chain)})


@app.route("/blockchain/add_transaction", methods=['GET'])
def add_transaction():
    blockchain.add_new_transaction(transaction1)
    return transaction1.get_transaction_data()


@app.route("/blockchain/mine_block", methods=['GET'])
def add_block():
    if blockchain.mine() is False:
        return "There are no transactions to put in the block!"
    block = blockchain.get_last_block()
    return json.dumps({"block_header": {
        "timestamp": block.block_header.timestamp,
        "previous_block_hash": block.block_header.previous_block_hash,
        "merkle_root": block.block_header.merkle_root
    }
    })


app.run(debug=True, port=5000)
