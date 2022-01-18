from flask import Flask, render_template, request
from blockchain import Blockchain
from transaction import Transaction
import json

app = Flask(__name__)

blockchain = Blockchain()


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/blockchain/show_chain", methods=['GET'])
def get_blockchain():
	chain = []
	for block in blockchain.chain:
		block_data = {
			"blockHeader": {
				"timestamp": block.block_header.timestamp,
				"previousBlockHash": block.block_header.previous_block_hash,
				"merkleRoot": block.block_header.merkle_root
			}
		}
		chain.append(block_data)
	return json.dumps(chain)


@app.route("/blockchain/add_transaction", methods=['POST'])
def add_transaction():
	transaction_request = request.get_json()
	transaction = Transaction(transaction_request.get('sender'), transaction_request.get('recipient'),
							  transaction_request.get('amount'))
	blockchain.add_new_transaction(transaction)
	return transaction.get_transaction_data()


@app.route("/blockchain/show_unverified_transactions", methods=['GET'])
def get_unverified_transactions():
	transactions = []
	for transaction_data in blockchain.unverified_transactions:
		transactions.append(transaction_data)
	return json.dumps(transactions)


@app.route("/blockchain/mine_block", methods=['GET'])
def add_block():
	if blockchain.mine() is False:
		return "There are no transactions to put in the block!"
	block = blockchain.get_last_block()
	return json.dumps({
		"block_header": {
			"timestamp": block.block_header.timestamp,
			"previous_block_hash": block.block_header.previous_block_hash,
			"merkle_root": block.block_header.merkle_root
		}
	})


app.run(debug=True, port=8000)
