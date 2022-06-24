
class Flat_Iterator:
	def __init__(self, data):
		self.data = data

	def __iter__(self):
		self.main_index = 0
		self.nested_index = -1
		return self

	def __next__(self):
		self.nested_index += 1
		if self.nested_index > len(self.data[self.main_index]) - 1:
			self.main_index += 1
			self.nested_index = 0
		if self.main_index > len(self.data) - 1:
			raise StopIteration
		return self.data[self.main_index][self.nested_index]

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]