import json
import unittest

from cryptocurrency.utils import compute_hash
from cryptocurrency.merkle_tree import get_merkle_root

TRANSACTION_DATA_1 = json.dumps({"Sender": "Address1", "Recipient": "Address2", "Amount": 200})
TRANSACTION_DATA_2 = json.dumps({"Sender": "Address1", "Recipient": "Address3", "Amount": 100})
TRANSACTION_DATA_3 = json.dumps({"Sender": "Address2", "Recipient": "Address3", "Amount": 50})

TRANSACTIONS_DATA_1 = [TRANSACTION_DATA_1]
TRANSACTIONS_DATA_2 = [TRANSACTION_DATA_1, TRANSACTION_DATA_2]
TRANSACTIONS_DATA_3 = [TRANSACTION_DATA_1, TRANSACTION_DATA_2, TRANSACTION_DATA_3]


class TestMerkleTree(unittest.TestCase):
    def test_merkle_root_when_one_transaction(self):
        leaf = compute_hash(TRANSACTIONS_DATA_1[0])
        self.assertEqual(leaf, get_merkle_root(TRANSACTIONS_DATA_1))

    def test_merkle_root_when_two_leaves(self):
        left_leaf = compute_hash(TRANSACTIONS_DATA_2[0])
        right_leaf = compute_hash(TRANSACTIONS_DATA_2[1])
        expected_merkle_root = compute_hash(left_leaf + right_leaf)
        merkle_root = get_merkle_root(TRANSACTIONS_DATA_2)
        self.assertEqual(expected_merkle_root, merkle_root)

    def test_merkle_root_when_three_transactions(self):
        leaf_0 = compute_hash(TRANSACTIONS_DATA_3[0])
        leaf_1 = compute_hash(TRANSACTIONS_DATA_3[1])
        leaf_2 = compute_hash(TRANSACTIONS_DATA_3[2])
        leaf_3 = compute_hash(TRANSACTIONS_DATA_3[2])

        parent_1 = compute_hash(leaf_0 + leaf_1)
        parent_2 = compute_hash(leaf_2 + leaf_3)

        expected_merkle_root = compute_hash(parent_1 + parent_2)
        merkle_root = get_merkle_root(TRANSACTIONS_DATA_3)

        self.assertEqual(expected_merkle_root, merkle_root)
