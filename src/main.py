import json
from flask import Flask, render_template, request
from transaction import Transaction
from blockchain import Blockchain


if __name__ == "__main__":

	app = Flask(__name__)
	blockchain = Blockchain()


	@app.route("/blockchain/show_chain", methods=['GET'])
	def get_blockchain() -> str:
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
		return json.dumps(chain, indent=4)


	@app.route("/blockchain/add_transaction", methods=['POST'])
	def add_transaction() -> str:
		transaction_request = request.get_json()
		transaction = Transaction(transaction_request.get('sender'), transaction_request.get('recipient'),
									transaction_request.get('amount'))
		blockchain.add_new_transaction(transaction)
		return json.dumps(transaction.get_transaction_data(), indent=4)


	@app.route("/blockchain/show_unverified_transactions", methods=['GET'])
	def get_unverified_transactions() -> str:
		return json.dumps(blockchain.get_unverified_transactions_content(), indent=4)


	@app.route("/blockchain/mine_block", methods=['GET'])
	def add_block() -> str:
		if blockchain.mine_block() is False:
			return "There are no transactions to put in the block!"
		block = blockchain.get_last_block()
		return json.dumps({
			"block_header": {
				"timestamp": block.block_header.timestamp,
				"previous_block_hash": block.block_header.previous_block_hash,
				"merkle_root": block.block_header.merkle_root
			}
		}, indent=4)


app.run(debug=True, port=8000)
