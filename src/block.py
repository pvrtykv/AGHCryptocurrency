import json
from utils import compute_hash
<<<<<<< HEAD

=======
>>>>>>> a200fa73c3ffcb4cf45f3e38b1f75d6cc5a47bc2

class Block:
    def __init__(self, timestamp, previous_block_hash, merkle_root):
        self.timestamp = timestamp
        self.previous_block_hash = previous_block_hash
        self.merkle_root = merkle_root

    def compute_block_hash(self):
        block_content = {
            "timestamp": self.timestamp,
            "previous_block_hash": self.previous_block_hash,
            "merkle_root": self.merkle_root
        }

        return compute_hash(json.dumps(block_content))

