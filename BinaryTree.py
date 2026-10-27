"""A simple binary tree and traversal examples."""


class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right
		self.parent = None
		if left is not None:
			left.parent = self
		if right is not None:
			right.parent = self

	
	def addChild(self, value):
		if value < self.value:
			if self.left is None:
				self.left = Node(value)
				self.left.parent = self
			else:
				self.left.addChild(value)
		else:
			if self.right is None:
				self.right = Node(value)
				self.right.parent = self
			else:
				self.right.addChild(value)
				
	@staticmethod
	def findRoot(node):
		"""Find the root of the binary tree."""
		while node is not None and node.parent is not None:
			node = node.parent
		return node.value if node is not None else None

#def findRoot():

def inorder(node, result=[]):
	"""Visit left subtree, node, then right subtree."""
	if node is None:
		return []
	inorder(node.left, result)
	result.append(node.value)
	inorder(node.right, result)
	return result


def preorder(node, result=[]):
	"""Visit node, left subtree, then right subtree."""
	if node is None:
		return []
	result.append(node.value)
	preorder(node.left, result)
	preorder(node.right, result)
	return result


def postorder(node, result=[]):
	"""Visit left subtree, right subtree, then node."""
	if node is None:
		return []
	postorder(node.left, result)
	postorder(node.right, result)
	result.append(node.value)
	return result

def build_tree(values):
	"""Build a binary search tree by inserting values in list order."""
	values = iter(values)
	try:
		root = Node(next(values))
	except StopIteration:
		return None
	for value in values:
		root.addChild(value)
	return root

def searchBST(root, target):
    node = root
    
    # Dokud nejsme na konci větve
    while node is not None:
        if target == node.value:
            return node        # Úspěch, našli jsme uzel
        elif target < node.value:
            node = node.left   # Jdeme doleva (hledáme menší číslo)
        else:
            node = node.right  # Jdeme doprava (hledáme větší číslo)
            
    return None  # Prošli jsme větev a prvek ve stromu není

def maxDepth(node):
    if node is None:
        return 0
    return 1 + max(maxDepth(node.left), maxDepth(node.right))

def print_parent_and_depth(node, depth=0):
	"""Print each node's value, parent, and depth (root depth is zero)."""
	if node is None:
		return
	parent_value = node.parent.value if node.parent is not None else None
	print(f"Value: {node.value}, Parent: {parent_value}, Depth: {depth}")
	print_parent_and_depth(node.left, depth + 1)
	print_parent_and_depth(node.right, depth + 1)


#          1
#         / \
#        2   3
#       / \   \
#      4   5   6
tree = Node(1, Node(2, Node(4), Node(5)), Node(3, right=Node(6)))

print(inorder(tree))    # [4, 2, 5, 1, 3, 6]
print(preorder(tree))   # [1, 2, 4, 5, 3, 6]
print(postorder(tree))  # [4, 5, 2, 6, 3, 1]

numbers = [8, 3, 10, 1, 6, 14, 4, 7, 13]
list_tree = build_tree(numbers)
print("\nTree built from:", numbers)
print_parent_and_depth(list_tree)

print("PostOrder:", postorder(list_tree))
print("PreOrder:", preorder(list_tree))