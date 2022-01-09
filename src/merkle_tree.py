import hashlib
import math


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def get_merkle_tree_depth(number_of_leaves):
    return math.ceil(math.log2(number_of_leaves))
