import math
from typing import List
from .utils import compute_hash


class Node:
	def __init__(self, value: str, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


def get_merkle_tree_depth(number_of_leaves: int) -> int:
	return math.ceil(math.log2(number_of_leaves))


def is_power_of_2(number: int) -> bool:
	return math.log2(number).is_integer()


def fill_transactions_list(transactions: List[str]) -> List[str]:
	previous_number_of_leaves = len(transactions)
	final_number_of_leaves = 2**get_merkle_tree_depth(previous_number_of_leaves)
	if previous_number_of_leaves % 2 == 0:
		for i in range(previous_number_of_leaves, final_number_of_leaves, 2):
			transactions = transactions + [transactions[-1], transactions[-2]]
	else:
		for i in range(previous_number_of_leaves, final_number_of_leaves):
			transactions.append(transactions[-1])
	return transactions


def build_merkle_tree(transactions: List[str]) -> Node:
	print("Building merkle tree...")
	if is_power_of_2(len(transactions)) is False:
		transactions = fill_transactions_list(transactions)
	leaves = []

	for transaction in transactions:
		leaves.append(Node(compute_hash(transaction)))

	if len(leaves) == 1:
		return leaves[0]

	tree_depth = get_merkle_tree_depth(len(leaves))
	nodes = []

	for i in range(0, tree_depth):
		nodes = []
		number_of_nodes = 2 ** (tree_depth - i)
		for j in range(0, number_of_nodes, 2):
			left_child = leaves[j]
			right_child = leaves[j + 1]
			node = Node(compute_hash(left_child.value + right_child.value), left_child, right_child)
			nodes.append(node)
		leaves = nodes
	return nodes[0]


def get_merkle_root(transactions: List[str]) -> str:
	merkle_tree = build_merkle_tree(transactions)
	return merkle_tree.value

