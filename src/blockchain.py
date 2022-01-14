from block import Block
import time

from merkle_tree import get_merkle_root
from block import Block


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()
        self.unverified_transactions = []

    def create_genesis_block(self):
        genesis_block = Block(time.time(), "", "")
        genesis_block.hash = genesis_block.compute_block_hash()
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]

    def create_new_block(self, block):
        self.chain.append(block)

    def add_new_transaction(self, transaction):
        self.unverified_transactions.append(transaction)

    def mine(self):
        if not self.unverified_transactions:
            return False

        last_block = self.get_last_block()

        new_block = Block(timestamp=time.time(), previous_block_hash=last_block.compute_block_hash(),
                          merkle_root=get_merkle_root(self.unverified_transactions))

        self.create_new_block(new_block)
        self.unverified_transactions = []
