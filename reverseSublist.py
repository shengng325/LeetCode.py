def reverseSublist(head, m, n):
        count = 1
        node = newHead = head
        prevNode = None
        while node is not None:
            nextNode = node.next
            if count == m:
                reversedHead = reverseSubList(node, n - m + 1)
                if m == 1:
                    newHead = reversedHead
                else:
                    prevNode.next = reversedHead
                break
            prevNode = node
            node = nextNode
            count+=1
        return newHead

def reverseSubList(head, count):
        prevNode = None
        curNode = head
        curCount = 1
        while curCount <= count:
            nextNode = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = nextNode
            curCount+=1
        head.next = curNode
        return prevNode

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

results = reverseSublist(head, 2, 4)
print(results)