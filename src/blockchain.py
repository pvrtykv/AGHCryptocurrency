from utils import dicts_to_strings
import time

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

    def create_new_block(self, block: Block):
        self.chain.append(block)

    def add_new_transaction(self, transaction: Transaction):
        self.unverified_transactions.append(transaction)

    def get_unverified_transactions_data(self):
        unverified_transactions_data = []
        for transaction in self.unverified_transactions:
            unverified_transactions_data.append(transaction.get_transaction_data())
        return unverified_transactions_data

    def mine(self):
        if not self.unverified_transactions:
            return False

        last_block = self.get_last_block()
        last_block_hash = last_block.block_header.compute_block_hash()
        merkle_root = get_merkle_root(dicts_to_strings(self.get_unverified_transactions_data()))
        new_block_header = BlockHeader(time.time(), last_block_hash, merkle_root)
        new_block = Block(new_block_header, self.unverified_transactions)

        self.create_new_block(new_block)
        self.unverified_transactions = []
