import unittest
from utils import compute_hash
from merkle_tree import get_merkle_root

transactions = ["A", "B"]
transaction = ["A"]
three_transactions = ["A", "B", "C"]


class TestMerkleTree(unittest.TestCase):
    def test_merkle_root_when_two_leaves(self):
        left_leaf = compute_hash(transactions[0])
        right_leaf = compute_hash(transactions[1])
        expected_merkle_root = compute_hash(left_leaf + right_leaf)
        merkle_root = get_merkle_root(transactions)
        self.assertEqual(expected_merkle_root, merkle_root)

    def test_merkle_root_when_one_transaction(self):
        leaf = compute_hash(transaction[0])
        self.assertEqual(leaf, get_merkle_root(transaction))

    def test_merkle_root_when_three_transactions(self):
        leaf_0 = compute_hash(three_transactions[0])
        leaf_1 = compute_hash(three_transactions[1])
        leaf_2 = compute_hash(three_transactions[2])
        leaf_3 = compute_hash(three_transactions[2])

        parent_1 = compute_hash(leaf_0 + leaf_1)
        parent_2 = compute_hash(leaf_2 + leaf_3)

        expected_merkle_root = compute_hash(parent_1 + parent_2)
        merkle_root = get_merkle_root(three_transactions)

        self.assertEqual(expected_merkle_root, merkle_root)