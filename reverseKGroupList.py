def reverseKGroupList(head, k):
        curNode = head
        newHead = None
        while curNode is not None:
            reversedHead, reversedTail = reverseSubList(curNode, k)
            prevNode = reversedTail
            curNode = reversedTail.next
            if newHead is None:
                newHead = reversedHead
            else:
                prevNode.next = reversedHead
        return newHead 


def reverseSubList(head, k):
        curNode = head
        prevNode = None
        count = 0
        while curNode is not None and count < k:
            count+=1
            prevNode = curNode
            curNode = curNode.next
        if count < k:
            return head, prevNode

        curNode = head
        prevNode = None
        count = 1
        while count <= k:
            nextNode = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = nextNode
            count+=1
        head.next = curNode
        return prevNode, head

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

k = 3
results = reverseKGroupList(head, k)
print(results)