import json
from .utils import compute_hash

DIFFICULTY = 2


class BlockHeader:
	def __init__(self, timestamp, previous_block_hash, merkle_root):
		self.timestamp = timestamp
		self.previous_block_hash = previous_block_hash
		self.merkle_root = merkle_root
		self.difficulty = DIFFICULTY
		self.nonce = 0
		self.hash = self.compute_block_hash()

	def get_block_header_content(self) -> dict:
		return {
			"timestamp": self.timestamp,
			"previous_block_hash": self.previous_block_hash,
			"merkle_root": self.merkle_root,
			"difficulty": self.difficulty,
			"nonce": self.nonce
		}

	def compute_block_hash(self) -> str:
		return compute_hash(json.dumps(self.get_block_header_content()))

	def mine(self, difficulty):
		while self.hash[:difficulty] != "0" * difficulty:
			print(f'Trying again... {self.hash}')
			self.nonce += 1
			self.hash = self.compute_block_hash()


class Block:
	def __init__(self, block_header: BlockHeader, transactions_data):
		self.block_header = block_header
		self.transactions_data = transactions_data
