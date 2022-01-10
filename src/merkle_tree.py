import math
from utils import compute_hash


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def get_merkle_tree_depth(number_of_leaves):
    return math.ceil(math.log2(number_of_leaves))


def is_power_of_2(number):
    return math.log2(number).is_integer()
# TODO: what to do when number of leaves is not power of 2


def build_merkle_tree(data: [str]):
    leaves = []
    for d in data:
        leaves.append(Node(compute_hash(d)))

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
