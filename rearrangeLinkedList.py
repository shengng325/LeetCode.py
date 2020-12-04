class LinkedList:
	def __init__(self, value):
		self.value = value
		self.next = None

def rearrangeLinkedList(head):
    slowNode = fastNode = head
    while fastNode is not None and fastNode.next is not None:
        slowNode = slowNode.next
        fastNode = fastNode.next.next
    
    reversedNode = reversedLinkedList(slowNode)

    node = head
    newHead = node

    while node is not None and reversedNode is not None:
        nextNode = node.next
        node.next = reversedNode
        nextReversedNode = reversedNode.next
        reversedNode.next = nextNode
        node = nextNode
        reversedNode = nextReversedNode
    if slowNode is not None:
        slowNode.next = None
    return newHead

def reversedLinkedList(head):
    prevNode = None
    curNode = head
    while curNode is not None:
        nextNode = curNode.next
        curNode.next = prevNode
        prevNode = curNode
        curNode = nextNode
    return prevNode

node0 = LinkedList(0)
node1 = LinkedList(1)
node2 = LinkedList(2)
node3 = LinkedList(3)
node4 = LinkedList(4)
node5 = LinkedList(5)
# node6 = LinkedList(6)

head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
# node5.next = node6

results = rearrangeLinkedList(head)
print(results)