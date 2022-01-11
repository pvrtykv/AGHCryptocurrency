from block import Block
import time

from merkle_tree import get_merkle_root


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(time.time(), "", "")
        genesis_block.hash = genesis_block.compute_block_hash()
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]

    def create_new_block(self, transactions):
        previous_block = self.get_last_block()
        block = Block(time.time(), previous_block.compute_block_hash(), get_merkle_root(transactions))
        self.chain.append(block)