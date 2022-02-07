import json
import time

from typing import List, Dict
from utils import dicts_to_strings
from merkle_tree import get_merkle_root
from block import Block, BlockHeader
from transaction import Transaction


class Blockchain:
	def __init__(self):
		self.chain = []
		self.create_genesis_block()
		self.unverified_transactions = []

	def create_genesis_block(self):
		genesis_block_header = BlockHeader(time.time(), "0", "")
		genesis_block = Block(genesis_block_header, "")
		self.chain.append(genesis_block)

	def get_last_block(self) -> Block:
		return self.chain[-1]

	def append_block(self, block: Block):
		self.chain.append(block)

	def add_new_transaction(self, transaction: Transaction):
		self.unverified_transactions.append(transaction)

	def get_unverified_transactions_content(self) -> List[dict]:
		unverified_transactions_data = []
		for transaction in self.unverified_transactions:
			unverified_transactions_data.append(transaction.get_transaction_data())
		return unverified_transactions_data

	def mine_block(self) -> bool:
		if not self.unverified_transactions:
			return False

		last_block = self.get_last_block()
		last_block_hash = last_block.block_header.hash
		print("Calculating merkle root of unverified transactions...")
		merkle_root = get_merkle_root(dicts_to_strings(self.get_unverified_transactions_content()))
		print(f'Calculated merkle root: {merkle_root}')
		new_block_header = BlockHeader(time.time(), last_block_hash, merkle_root)
		print("---------------------------------------------------------")
		print("Mining block...")
		new_block_header.mine(new_block_header.difficulty)
		new_block = Block(new_block_header, self.unverified_transactions)
		new_block_header_content = new_block_header.get_block_header_content()
		new_block_header_content["hash"] = new_block_header.hash
		print("Mined block:")
		print(json.dumps(new_block_header_content, indent=4))

		self.append_block(new_block)
		self.unverified_transactions = []
		return True

	def get_blockchain_content(self) -> List[Dict]:
		blockchain_content = []
		for block in self.chain:
			block_header_content = block.block_header.get_block_header_content()
			block_header_content["hash"] = block.block_header.hash
			blockchain_content.append(block_header_content)
		return blockchain_content
