# Use pass by reference to search in BST
def findClosestValueInBst1(tree, target):
	closest = Closest()
	findClosestHelper1(tree, target, closest)
	return closest.value

def findClosestHelper1(tree, target, closest):
	if tree is None:
		return
	closest.value = min(closest.value, tree.value, key=lambda x: abs(target - x))
	if target < tree.value:
		findClosestHelper1(tree.left, target, closest)
	else:
		findClosestHelper1(tree.right, target, closest)

class Closest:
	def __init__ (self):
		self.value = float("inf")

# Use return value to search in BST
def findClosestValueInBst2(tree, target):
	return findClosestHelper2(tree, target, tree.value)

def findClosestHelper2(tree, target, closest):
	if tree is None:
		return closest
	closest = min(closest, tree.value, key=lambda x: abs(x - target))
	if target < tree.value:
		leafClosest = findClosestHelper2(tree.left, target, closest)
	else:
		leafClosest = findClosestHelper2(tree.right, target, closest)
	return 	min(closest, leafClosest, key=lambda x: abs(x - target))

# Use iterative
def findClosestValueInBst(tree, target):
	closest = tree.value
	node = tree
	while node is not None:
		closest = min(closest, node.value, key=lambda x: abs(x - target))
		if target < node.value:
			node = node.left
		else:
			node = node.right
	return closest

tree = None 
target = 0
results = findClosestValueInBst(tree, target)
print(results)