# Use Tkinter for python 2, tkinter for python 3
import tkinter as tk
from tkinter import filedialog as fd


from checky import Checky

class CheckyGUI():
	def __init__(self, master, *args, **kwargs):

	# tk Vars
		self.last_code = tk.StringVar()
		self.sound_on_var = tk.BooleanVar()

	# Main Frame
		self.master = master

	# Sub Frames
		#self.top_frame = tk.Frame(master=self.master)
		self.left_frame = tk.Frame(master=self.master)
		self.right_frame = tk.Frame(master=self.master)
		self.bottom_frame = tk.Frame(master=self.master)

	# Top Frame Widgets

	# Left Frame Widgets
		self.load_batch_found = tk.Button(master=self.left_frame,
			text="Load Found", command=self.load_batch_found_file)
		self.found_text = tk.Text(master=self.left_frame, state=tk.DISABLED,
			bg="GREEN", relief="sunken")
		self.found_text.bind("<1>", lambda event: self.found_text.focus_set())

	# Right Frame Widgets
		self.load_missing = tk.Button(master=self.right_frame,
			text="Load Missing", command=self.load_missing_file)
		self.missing_text = tk.Text(master=self.right_frame, state=tk.DISABLED,
			bg="RED")
		self.missing_text.bind("<1>", lambda event: self.missing_text.focus_set())

	# Bottom Frame Widgets
		self.sound_on_box = tk.Checkbutton(master=self.bottom_frame,
			text="Sound", variable=self.sound_on_var, onvalue=True,
				offvalue=False)
		self.search_button = tk.Button(master=self.bottom_frame, text="Search",
			command=self.search)
		self.single_entry = tk.Entry(master=self.bottom_frame)
		self.last_entry_label = tk.Text(master=self.bottom_frame, height=1,
			width=12, state=tk.DISABLED)

# Layout
	# Sub Frames
		#self.top_frame.grid(row=0, column=0, columnspan=2, sticky=tk.N)
		self.left_frame.grid(row=1, column=0, sticky=tk.N)
		self.right_frame.grid(row=1, column=1, sticky=tk.N)
		self.bottom_frame.grid(row=2, column=0, columnspan=2)

		# Top Frame Layout

		# Left Frame Layout
		self.load_batch_found.grid(row=0, column=0, sticky=(tk.N, tk.S))
		self.found_text.grid(row=1, column=0, sticky=(tk.N, tk.E, tk.S, tk.W))
		
		# Right Frame Layout
		self.load_missing.grid(row=0, column=0, sticky=(tk.N, tk.S))
		self.missing_text.grid(row=1, column=0, sticky=(tk.N, tk.E, tk.S, tk.W))
		
		# Bottom Frame Layout
		self.sound_on_box.grid(row=0, column=0, sticky=tk.N)
		self.search_button.grid(row=0, column=1, sticky=tk.N)
		self.single_entry.grid(row=0, column=2, sticky=tk.N)
		self.last_entry_label.grid(row=0, column=3, sticky=tk.N)

# Weights
		#self.master.columnconfigure(0, weight=1)
		#self.master.columnconfigure(1, weight=1)
		#self.master.rowconfigure(0, weight=1)
		#self.master.rowconfigure(1, weight=1)
		#self.left_frame.columnconfigure(0, weight=1)
		#self.left_frame.columnconfigure(1, weight=1)
		#self.left_frame.rowconfigure(0, weight=1)
		#self.left_frame.rowconfigure(2, weight=1)
		#self.right_frame.columnconfigure(0, weight=1)
		#self.right_frame.columnconfigure(1, weight=1)
		#self.right_frame.rowconfigure(0, weight=1)
		#self.right_frame.rowconfigure(2, weight=1)
		#self.found_text.columnconfigure(0, weight=1)



# Key Bindings
		master.bind('<Return>', self.search)

# Functionality
		self.checky = Checky()
		
	# Missing 
	def load_missing_file(self):
		"""Loads missing data from a CSV file into the 'Missing' object."""
		filename = fd.askopenfilename(initialdir="/Desktop",
			title="Select csv file", filetypes=(("csv files","*.csv"),
				("all files","*.*")))
		self.checky.load_missing_file(filename)
		self.update_text()

	
	# Found
	def load_batch_found_file(self):
		"""Loads a batch of found data from a text file."""
		filename = fd.askopenfilename(initialdir="/Desktop",
			title="Select csv file", filetypes=(("txt files","*.txt"),
				("all files","*.*")))
		self.checky.load_batch_found_file(filename)
		self.update_text()

	def update_text(self):
		"""Updates both text fields."""
		self.update_found_text()
		self.update_missing_text()

	def update_found_text(self):
		"""Updates the 'Found' data text field."""
		self.found_text.config(state=tk.NORMAL)
		self.found_text.delete(1.0, tk.END)
		for barcode, description in self.checky.found.data.items():
			self.found_text.insert(tk.INSERT, barcode + ':' + description
				+ '\n')
		self.found_text.config(state=tk.DISABLED)
	
	def update_missing_text(self):
		"""Updates the 'missing' data text field."""
		self.missing_text.config(state=tk.NORMAL)
		self.missing_text.delete(1.0, tk.END)
		for barcode, description in self.checky.missing.data.items():
			self.missing_text.insert(tk.INSERT, barcode + ':' + description
				+ '\n')
		self.missing_text.config(state=tk.DISABLED)

	def update_last_entry(self, code):
		self.last_entry_label.config(state=tk.NORMAL)
		self.last_entry_label.delete(1.0, tk.END)
		self.last_entry_label.insert(tk.INSERT, code)
		self.last_entry_label.config(state=tk.DISABLED)

	def entry_state(self):
		if self.checky.single_code_flag:
			self.last_entry_label.config(fg='GREEN')
		else:
			self.last_entry_label.config(fg='RED')



	def search(self, event=None):
		code = self.single_entry.get()
		self.checky.sound_on = self.sound_on_var.get()
		self.checky.single_check(code)
		self.entry_state()
		self.update_last_entry(code)
		self.update_text()
		self.single_entry.delete(0, tk.END)
		





if __name__ == "__main__":
	root = tk.Tk()
	checky_app = CheckyGUI(root)
	root.mainloop()