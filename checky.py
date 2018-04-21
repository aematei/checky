from missing import Missing
from found import Found 
import simpleaudio as sa
import csv

class Checky():
	"""The checky main app"""
	def __init__(self):
		"""Initialize Checky instance"""

		self.found = Found()
		self.missing = Missing(self.found)
		
		# Was the last scanned code in missing? Boolean.
		self.single_code_flag = False
		
		# Single entry sound options.
		self.sound_on = False
		self.yes_sound = sa.WaveObject.from_wave_file("audio/Yes.wav")
		self.no_sound = sa.WaveObject.from_wave_file("audio/No.wav")
		
#Core Functions (linked to GUI) 	

	def load_missing_file(self, filename):
		"""Loads missing data from a CSV file into the 'Missing' object."""
		self.missing.populate(filename)
		self.update_missing_load()
		
	def load_batch_found_file(self, filename):
		"""Loads a batch of found data from a text file."""
		self.found.populate(filename)
		self.check_found_load()

	def single_check(self, code):
		"""
		Checks if single entry input is in found or missing data and 
		plays audio if the option is enabled by the user.
		"""
		if code not in self.found.data:
			if code in self.missing.data:
				self.found.data[code] = self.missing.data.pop(code)
				self.single_code_flag = True
				if self.sound_on:
					self.yes_sound.play()
			else:
				self.single_code_flag = False
				if self.sound_on:
					self.no_sound.play()
		elif code in self.found.data:
			if self.sound_on:
				self.yes_sound.play()

	def save_missing(self, filename):
		"""Saves missing data in a two column csv doc."""
		file = open(filename, 'w')
		with file:
			writer = csv.writer(file)
			writer.writerow(['Barcodes', 'Description'])
			for barcode, description in self.missing.data.items():
				datum = [barcode, description]
				writer.writerow(datum)

# Sub Functions (used by checky class only)

	def update_missing_load(self):
		"""Removes missing.data if it's already in found.data"""
		for datum in self.found.data:
			if datum in self.missing.data:
				del self.missing.data[datum]

	def check_found_load(self):
		"""
		Checks if found.check_these is in
		missing.data and moves data if it is.
		"""
		for datum in self.found.check_these:
			if datum in self.missing.data:
				if datum not in self.found.data:
					self.found.data[datum] = self.missing.data.pop(datum)
