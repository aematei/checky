import csv

class Missing():
	"""A object in which to store a dictionary of barcodes to find"""
	def __init__(self, found):
		self.data = {}
		self.found = found
	
	def populate(self, filename):
		""" 
		Takes a barcode vs. description csv file and
		populates a dictionary as {barcode: description}
		"""
		reader = csv.DictReader(open(str(filename)))
		result = {}
		for row in reader:
			if row not in self.found.data.items():
				for column, value in row.items():
					result.setdefault(column, []).append(value.rstrip())
		# Check for duplicates before adding result to missing data.
		for datum in result:
			if datum not in self.data:
				self.data.update(dict(zip(result['Barcode'],
					result['Description'])))

