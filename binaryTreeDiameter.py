class Solution:
    def binaryTreeDiameter(self, root):
        treeInfo = TreeInfo(0, 0)
        self.binaryTreeDiameterHelper(root, 0, 0, treeInfo)
        return treeInfo.diameter

    def binaryTreeDiameterHelper(self, node, curHeight, curDiameter, treeInfo):
        if node is None:
            return TreeInfo(-1, 0)
        curValue = node.value
        print(curValue)
        leftHeight = self.binaryTreeDiameterHelper(node.left, curHeight, curDiameter, treeInfo).height
        rightHeight = self.binaryTreeDiameterHelper(node.right, curHeight, curDiameter, treeInfo).height
        curHeight = max(leftHeight, rightHeight) + 1
        curDiameter = curHeight + min(leftHeight, rightHeight) + 1
        treeInfo.height = curHeight
        treeInfo.diameter = max(treeInfo.diameter, curDiameter)
        return treeInfo

class TreeInfo:
    def __init__(self, height, diameter):
        self.height = height
        self.diameter = diameter


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
results = s.binaryTreeDiameter(root)
print(results)