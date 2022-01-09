from block import Block
import time


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(time.time(), "", "")
        genesis_block.hash = genesis_block.compute_block_hash()
        self.chain.append(genesis_block)
