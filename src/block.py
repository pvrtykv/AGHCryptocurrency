import json
from hashlib import sha256


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

        return sha256(json.dumps(block_content).encode()).hexdigest()

