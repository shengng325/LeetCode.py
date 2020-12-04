def linkedListCycle(head):
    slowNode = fastNode = head
    while fastNode is not None or fastNode.next is not None:
        slowNode = slowNode.next
        fastNode = fastNode.next.next
        if slowNode == fastNode:
            return False
    return True


head = None
results = linkedListCycle(head)
print(results)