class ContinuousMedianHandler:
	def __init__(self):
		# Write your code here.
		self.median = None
		self.greaterHeap = Heap(MIN_HEAP_FUNC, [])
		self.smallerHeap = Heap(MAX_HEAP_FUNC, [])

	def insert(self, number):
		if len(self.smallerHeap.heap) <= 0:
			self.smallerHeap.insert(number)
		elif number < self.smallerHeap.peek(): 
			self.smallerHeap.insert(number)
			if len(self.smallerHeap.heap) - len(self.greaterHeap.heap) > 1:
				removedValue = self.smallerHeap.remove()
				self.greaterHeap.insert(removedValue)
		else:
			self.greaterHeap.insert(number)
			if len(self.greaterHeap.heap) > len(self.smallerHeap.heap):
				removedValue = self.greaterHeap.remove()
				self.smallerHeap.insert(removedValue)
		if len(self.smallerHeap.heap) > len(self.greaterHeap.heap):
			self.median = self.smallerHeap.peek()
		else:
			self.median = (self.smallerHeap.peek() + self.greaterHeap.peek())/ 2

	def getMedian(self):
		return self.median

class Heap:
	def __init__(self, compareFunc, array):
		self.compare = compareFunc
		self.heap = self.buildHeap(array)

	def buildHeap(self, array):
		lastIdx = len(array) - 1
		firstParentIdx = (lastIdx - 1) //2
		for i in reversed(range(firstParentIdx + 1)):
			self.siftDown(i, len(array) - 1, array)
		return array

	def siftDown(self, curIdx, endIdx, heap):
		childIdxOne = 2*curIdx + 1
		while childIdxOne <= endIdx:
			childIdxTwo = 2*curIdx + 2 if 2*curIdx + 2 <= endIdx else -1
			if childIdxTwo != -1 and self.compare(heap[childIdxTwo], heap[childIdxOne]):
				idxToSwap = childIdxTwo
			else:
				idxToSwap = childIdxOne
			if self.compare(heap[idxToSwap], heap[curIdx]):
				self.swap(curIdx, idxToSwap, heap)
				curIdx = idxToSwap
				childIdxOne = 2*curIdx + 1
			else:
				break

	def siftUp(self, curIdx, heap):
		parentIdx = (curIdx - 1) // 2
		while curIdx > 0 and self.compare(heap[curIdx], heap[parentIdx]):
			self.swap(parentIdx, curIdx, heap)
			curIdx = parentIdx
			parentIdx = (curIdx - 1) // 2
			
	def peek(self):
		return self.heap[0]
	
	def remove(self):
		self.swap(0, -1, self.heap)
		valueRemoved = self.heap.pop()
		self.siftDown(0, len(self.heap) - 1, self.heap)
		return valueRemoved

	def insert(self, value):
		self.heap.append(value)
		self.siftUp(len(self.heap) - 1, self.heap)
	
	def swap(self, i, j, heap):
		heap[i], heap[j] = heap[j], heap[i]

def MAX_HEAP_FUNC(a, b):
	return a > b

def MIN_HEAP_FUNC(a, b):
	return a < b

median = ContinuousMedianHandler()
median.insert(5)
median.insert(10)
print(median.getMedian())
median.insert(100)
print(median.getMedian())