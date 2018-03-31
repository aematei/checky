from missing import Missing
from found import Found 

class Checky():
	"""The checky main app"""
	def __init__(self):

		self.found = Found()
		self.missing = Missing(self.found)
		
#### CORE FUNCTIONS 	

	def load_missing_file(self, filename):
		"""Loads missing data from a CSV file into the 'Missing' object."""
		self.missing.populate(filename)
		self.update_missing_load()
		print(self.missing.data)

	def load_batch_found_file(self, filename):
		"""Loads a batch of found data from a text file."""
		self.found.populate(filename)
		self.check_found_load()
		
#### SUB FUNCTIONS

#	def populate_missing(self, filename):
#		""" 
#		Takes a barcode vs. description csv file and
#		populates a dictionary as {barcode: description}
#		"""
#		reader = csv.DictReader(open(str(filename)))
#		result = {}
#		for row in reader:
#			if row not in self.found.data.items():
#				for column, value in row.items():
#					result.setdefault(column, []).append(value.rstrip())
#		self.missing.data.update(dict(zip(result['Barcode'],
#			result['Description'])))

	def update_missing_load(self):
		"""Removes missing.data if it's already in found.data"""
		for datum in self.found.data:
			if datum in self.missing.data:
				del self.missing.data[datum]

	def check_found_load(self):
		"""Checks if found.check_these is in missing.data and moves data if it is."""
		for datum in self.found.check_these:
			if datum in self.missing.data:
				if datum not in self.found.data:
					self.found.data[datum] = self.missing.data.pop(datum)

