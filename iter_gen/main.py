from gen import Flat_Generator
from iter import Flat_Iterator

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

if __name__ == '__main__':
	gen_list = [item for item in Flat_Generator(nested_list)]
	print(gen_list)
	for item in Flat_Generator(nested_list):
		print(item)
	iter_list = [item for item in Flat_Iterator(nested_list)]
	print(iter_list)
	for item in Flat_Iterator(nested_list):
		print(item)