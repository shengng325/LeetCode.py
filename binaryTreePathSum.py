def binaryTreePathSum(root, targetSum):
    if root is None:
        return False
    if root.left is None and root.right is None and root.value == targetSum:
        return True
    targetSum-=root.value
    return binaryTreePathSum(root.left, targetSum) or binaryTreePathSum(root.right, targetSum)

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

node1 = BinaryTree(1)
node2 = BinaryTree(2)
node3 = BinaryTree(3)
node4 = BinaryTree(4)
node5 = BinaryTree(5)
node6 = BinaryTree(6)
node7 = BinaryTree(7)

root = node1
root.left = node2
root.right = node3
root.left.left = node4
root.left.right = node5
root.right.left = node6
root.right.right = node7

targetSum = 10
results = binaryTreePathSum(root, targetSum)
print(results)