def rightSideView(self, root):
    if root is None:
        return []
    queue = [[root]]
    rightView = []
    while len(queue):
        curLevel = queue.pop(0)
        if len(curLevel) > 0:
            rightView.append(curLevel[-1].val)
        childLevel = []
        for node in curLevel:
            if node.left:
                childLevel.append(node.left)
            if node.right:
                childLevel.append(node.right)
        if len(childLevel) > 0:
            queue.append(childLevel)
    return rightView