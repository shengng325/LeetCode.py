def linkedListPalindrome(head):
	slowNode = fastNode = head
	while fastNode is not None and fastNode.next is not None:
		slowNode = slowNode.next
		fastNode = fastNode.next.next
	
	reverseList = reverseLinkedList(slowNode)
	node = head
	while reverseList is not None:
		if node.value != reverseList.value:
			return False
		node = node.next
		reverseList = reverseList.next
	return True
	
def reverseLinkedList(node):
	prevNode = None
	curNode = node
	while curNode is not None:
		nextNode = curNode.next
		curNode.next = prevNode
		prevNode = curNode
		curNode = nextNode
	return prevNode

head = None
results = linkedListPalindrome(head)
print(results)