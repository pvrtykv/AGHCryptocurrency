import unittest
from utils import compute_hash
from merkle_tree import get_merkle_root

transactions = ["A", "B"]


class TestMerkleTree(unittest.TestCase):
    def test_merkle_root_when_two_leaves(self):
        left_leaf = compute_hash(transactions[0])
        right_leaf = compute_hash(transactions[1])
        expected_merkle_root = compute_hash(left_leaf + right_leaf)
        merkle_root = get_merkle_root(transactions)
        self.assertEqual(expected_merkle_root, merkle_root)