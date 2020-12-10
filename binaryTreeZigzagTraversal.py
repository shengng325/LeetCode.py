def binaryTreeZigzagTraversal(root):
    queue = [root]
    zigzag = []
    i = 0
    isLeftFirst = True
    while i < len(queue):
        levelValues = []
        levelSize = len(queue) - i
        for _ in range(levelSize):
            if isLeftFirst:
                levelValues.append(queue[i].value)
            else:
                levelValues.insert(0, queue[i].value)    
            if queue[i].left is not None:
                queue.append(queue[i].left)
            if queue[i].right is not None:
                queue.append(queue[i].right)
            i+=1 
        isLeftFirst = not isLeftFirst
        zigzag.append(levelValues)
    return zigzag

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

root = node1
root.left = node2
root.right = node3
root.left.left = node4
root.left.right = node5
root.right.left = node6
root.right.right = node7
root.left.left.left = node8

results = binaryTreeZigzagTraversal(root)
print(results)