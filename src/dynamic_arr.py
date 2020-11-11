class DynamicArray(object):
​
	def __init__(self, capacity=10):
​
		self.size = 0
		self.capacity = capacity
		self.storage =  [None] * capacity
​
	def __len__(self):
		return self.size
​
	def __getitem__(self, idx):
​
		if not 0 <= idx < self.size:
			return IndexError('index is out of bounds!')
​
		return self.storage[idx]
​
	def append(self, elem):
​
		if self.size == self.capacity:
			self._grow(2 * self.capacity) # 2 x if capacity isn't enough
		
		self.storage[self.size] = elem
		self.size += 1
​
​
	def _grow(self, new_capacity):
​
		new_array = [None] * new_capacity
​
		for i in range(self.size):
			new_array[i] = self.capacity[i]
​
		self.storage = new_array
		self.capacity = new_capacity
​
​
arr = DynamicArray()
arr.append(1)
arr.append(231)
arr.append("food")
​
print(len(arr))
print(arr[2])
C