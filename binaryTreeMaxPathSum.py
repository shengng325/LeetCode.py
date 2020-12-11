class Solution:
    def binaryTreeMaxPathSum(self, root):
        maxSum = MaxSum()
        self.maxPathSumHelper(root, maxSum)
        return maxSum.value

    def maxPathSumHelper(self, node, maxSum):
        if node is None:
            return 0
        leftSum = self.maxPathSumHelper(node.left, maxSum)
        rightSum = self.maxPathSumHelper(node.right, maxSum)
        curSum = leftSum + rightSum + node.value
        maxSum.value = max(maxSum.value, curSum, leftSum + node.value, rightSum + node.value, node.value)
        return max(leftSum + node.value, rightSum + node.value, node.value)

class MaxSum:
    def __init__(self):
        self.value = 0

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
node8 = BinaryTree(8)
node9 = BinaryTree(9)
node10 = BinaryTree(10)
node11 = BinaryTree(11)

root = node1
root.left = node2
root.right = node3
root.left.left = node4
root.right.left = node5
root.right.right = node6
root.right.left.left = node7
root.right.left.right = node8
root.right.right.left = node9
root.right.left.right.left = node10
root.right.right.left.right = node11

s = Solution()
results = s.binaryTreeMaxPathSum(root)
print(results)