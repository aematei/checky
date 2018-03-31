# Use Tkinter for python 2, tkinter for python 3
import tkinter as tk
from tkinter import filedialog as fd

import csv

from missing import Missing
from found import Found

class Checky():
	def __init__(self, master, *args, **kwargs):
	# Main Frame
		self.master = master

	# Sub Frames
		self.top_frame = tk.Frame(master=self.master)
		self.left_frame = tk.Frame(master=self.master)
		self.right_frame = tk.Frame(master=self.master)
		self.bottom_frame = tk.Frame(master=self.master)

	# Top Frame Widgets

	# Left Frame Widgets
		self.load_batch_found = tk.Button(master=self.left_frame,
			text="Load Found", command=self.load_batch_found_file)
		self.found_text = tk.Text(master=self.left_frame, state=tk.DISABLED,
			bg="GREEN")

	# Right Frame Widgets
		self.load_missing = tk.Button(master=self.right_frame,
			text="Load Missing", command=self.load_missing_file)
		self.missing_text = tk.Text(master=self.right_frame, state=tk.DISABLED,
			bg="RED")

	# Bottom Frame Widgets
		self.search_button = tk.Button(master=self.bottom_frame, text="Search")
		self.single_entry = tk.Entry(master=self.bottom_frame)


# Layout
	# Sub Frames
		self.top_frame.grid(row=0, column=0, columnspan=2)
		self.left_frame.grid(row=1, column=0)
		self.right_frame.grid(row=1, column=1)
		self.bottom_frame.grid(row=2, column=0, columnspan=2)

		# Top Frame Layout

		# Left Frame Layout
		self.load_batch_found.grid(row=0, column=0)
		self.found_text.grid(row=1, column=0)
		
		# Right Frame Layout
		self.load_missing.grid(row=0, column=0)
		self.missing_text.grid(row=1, column=0)
		
		# Bottom Frame Layout
		self.search_button.grid(row=0, column=0)
		self.single_entry.grid(row=0, column=1)

# Functionality
		self.missing = Missing()
		self.found = Found()

	# Missing 
	def load_missing_file(self):
		"""Loads missing data from a CSV file into the 'Missing' object."""
		filename = fd.askopenfilename(initialdir="/Desktop",
			title="Select csv file", filetypes=(("csv files","*.csv"),
				("all files","*.*")))
		self.populate_missing(filename)
		self.check_missing_load()
		self.update_text()

	def populate_missing(self, filename):
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
		self.missing.data.update(dict(zip(result['Barcode'],
			result['Description'])))

	def update_missing_text(self):
		"""Updates the 'missing' data text field."""
		self.missing_text.config(state=tk.NORMAL)
		self.missing_text.delete(1.0, tk.END)
		for barcode, description in self.missing.data.items():
			self.missing_text.insert(tk.INSERT, barcode + ':' + description
				+ '\n')
		self.missing_text.config(state=tk.DISABLED)

	# Found
	def load_batch_found_file(self):
		"""Loads a batch of found data from a text file."""
		filename = fd.askopenfilename(initialdir="/Desktop",
			title="Select csv file", filetypes=(("txt files","*.txt"),
				("all files","*.*")))
		#print(filename)
		self.found.batch(filename)
		self.check_found_load()
		self.update_text()

	def update_found_text(self):
		"""Updates the 'Found' data text field."""
		self.found_text.config(state=tk.NORMAL)
		self.found_text.delete(1.0, tk.END)
		for barcode, description in self.found.data.items():
			self.found_text.insert(tk.INSERT, barcode + ':' + description
				+ '\n')
		self.found_text.config(state=tk.DISABLED)
		

	def check_found_load(self):
		"""Checks if found.check_these is in missing.data."""
		for datum in self.found.check_these:
			if datum in self.missing.data:
				if datum not in self.found.data:
					self.found.data[datum] = self.missing.data.pop(datum)


	def check_missing_load(self):
		"""Checks if new missing data is in missing.data."""
		for datum in self.found.data:
			if datum in self.missing.data:
				del self.missing.data[datum]
		
		
	def update_text(self):
		"""Updates both text fields."""
		self.update_found_text()
		self.update_missing_text()



if __name__ == "__main__":
	root = tk.Tk()
	checky = Checky(root)
	root.mainloop()