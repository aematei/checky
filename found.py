class Found():
	"""An object to store found data."""
	def __init__(self):
		self.check_these = []
		self.data = {}

	
	def batch(self, filename):
		file = open(filename, 'r') 
		load_data = [line.rstrip() for line in file]
		for datum in load_data:
			if datum not in self.data.items():
				self.check_these.append(datum)
				

# Next step: Make function that checks barcodes and adds found barcodes to data.