import json
from utils import compute_hash

class Block:
    def __init__(self, timestamp, transaction_data, previous_block_hash):
        self.timestamp = timestamp
        self.transaction_data = transaction_data
        self.previous_block_hash = previous_block_hash

    def compute_block_hash(self):
        block_content = {
            "timestamp": self.timestamp,
            "transaction_data": self.transaction_data,
            "previous_block_hash": self.previous_block_hash
        }

        return compute_hash(json.dumps(block_content))

