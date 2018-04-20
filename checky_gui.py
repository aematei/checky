import tkinter as tk
from tkinter import filedialog as fd

from checky import Checky


class CheckyGUI():
	def __init__(self, master, *args, **kwargs):

# Widgets 

	# Main Frame
		self.master = master

	# Sub Frames

		self.top_frame = tk.Frame(master=self.master)

		self.load_frame_left = tk.Frame(master=self.master)
		self.load_frame_right = tk.Frame(master=self.master)

		self.text_frame_left = tk.LabelFrame(master=self.master)
		self.text_frame_right = tk.LabelFrame(master=self.master)

		self.bottom_frame = tk.Frame(master=self.master)

		self.x_scroll_left = tk.Scrollbar(master=self.text_frame_left,
			orient=tk.HORIZONTAL)
		self.y_scroll_left = tk.Scrollbar(master=self.text_frame_left)

		self.x_scroll_right = tk.Scrollbar(master=self.text_frame_right,
			orient=tk.HORIZONTAL)
		self.y_scroll_right = tk.Scrollbar(master=self.text_frame_right)

	# Menu Bar
		self.menubar = tk.Menu(master=self.top_frame)
		self.filemenu = tk.Menu(self.menubar, tearoff=0)
		self.filemenu.add_command(label="New Session")
		self.filemenu.add_command(label="Load")
		self.filemenu.add_command(label="Save")
		self.filemenu.add_command(label="Print...")
		self.filemenu.add_command(label="Quit")
		self.menubar.add_cascade(label="File", menu=self.filemenu)
		
		self.master.config(menu=self.menubar)

	# Text Widgets 
		self.load_batch_found = tk.Button(master=self.load_frame_left,
			text="Load Found", command=self.load_batch_found_file)
		self.found_text = tk.Text(master=self.text_frame_left,
			state=tk.DISABLED, height=500)

		self.load_missing = tk.Button(master=self.load_frame_right,
			text="Load Missing", command=self.load_missing_file)
		self.missing_text = tk.Text(master=self.text_frame_right,
			state=tk.DISABLED)	

		self.y_scroll_right.config(command=self.missing_text.yview)
		self.x_scroll_right.config(command=self.missing_text.xview)

		self.y_scroll_left.config(command=self.missing_text.yview)
		self.x_scroll_left.config(command=self.missing_text.xview)
		
	# Bottom Frame Widgets
		self.sound_on_var = tk.BooleanVar()
		self.sound_on_box = tk.Checkbutton(master=self.bottom_frame,
			text="Sound", variable=self.sound_on_var, onvalue=True,
			offvalue=False)
		self.search_button = tk.Button(master=self.bottom_frame, text="Search",
			command=self.search)
		self.single_entry = tk.Entry(master=self.bottom_frame)
		self.last_entry_label = tk.Text(master=self.bottom_frame, height=1,
			width=12, state=tk.DISABLED)


# Styling

	# Colors
		self.bg_tan = '#e5e1da'
		self.bg_green = '#f7fff7'
		self.bg_red = '#fff7f7'

	# Top Frame Styling

		self.master["bg"] = self.bg_tan
		self.top_frame.config(bg=self.bg_tan)
		self.load_frame_left.config(bg=self.bg_tan)
		self.load_frame_right.config(bg=self.bg_tan)
		self.bottom_frame.config(bg=self.bg_tan)

	# Text Frames Styling

		self.load_frame_left.config(bg=self.bg_tan)
		self.load_frame_right.config(bg=self.bg_tan)
		self.load_batch_found.config(bg=self.bg_tan, highlightthickness=0,
			highlightbackground=self.bg_tan)
		self.found_text.config(relief="sunken", bg=self.bg_green,
			highlightbackground=self.bg_green)
		self.load_missing.config(bg=self.bg_tan, highlightthickness=0,
			highlightbackground=self.bg_tan)
		self.missing_text.config(bg=self.bg_red,
			highlightbackground=self.bg_red)

	# Bottom Frame Styling

		self.bottom_frame.config(bg=self.bg_tan)
		self.sound_on_box.config(bg=self.bg_tan, highlightthickness=0)
		self.search_button.config(bg=self.bg_tan, highlightthickness=0,
			highlightbackground=self.bg_tan)
		self.single_entry.config(highlightbackground=self.bg_tan,
			relief="sunken")
		self.last_entry_label.config(bg=self.bg_tan, highlightthickness=0)


# Layout
	
	# Sub Frames
		self.top_frame.grid(row=0, column=0, columnspan=3,
			sticky=(tk.N, tk.E, tk.W))

		self.load_frame_left.grid(row=1, column=0,
			sticky=(tk.N, tk.E, tk.S, tk.W))
		self.load_frame_right.grid(row=1, column=2,
			sticky=(tk.N, tk.E, tk.S, tk.W))

		self.text_frame_left.grid(row=2, column=0,
			sticky=(tk.N, tk.E, tk.S, tk.W))
		self.text_frame_right.grid(row=2, column=2,
			sticky=(tk.N, tk.E, tk.S, tk.W))

		self.bottom_frame.grid(row=4, column=0, columnspan=3,
			sticky=(tk.E, tk.S, tk.W))

		self.x_scroll_left.pack(side=tk.BOTTOM, fill=tk.X)
		self.y_scroll_left.pack(side=tk.RIGHT, fill=tk.Y)

		self.x_scroll_right.pack(side=tk.BOTTOM, fill=tk.X)
		self.y_scroll_right.pack(side=tk.RIGHT, fill=tk.Y)

	# Left Frame Layout
		self.load_batch_found.pack()
		self.found_text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

	# Right Frame Layout
		self.load_missing.pack()
		self.missing_text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
		
	# Bottom Frame Layout
		self.sound_on_box.grid(row=0, column=0, sticky=tk.S)
		self.search_button.grid(row=0, column=1, sticky=tk.S)
		self.single_entry.grid(row=0, column=2, sticky=tk.S)
		self.last_entry_label.grid(row=0, column=3, sticky=(tk.S, tk.N))

	# Weights
		self.master.columnconfigure(0, weight=1)
		self.master.columnconfigure(1, weight=1)
		self.master.columnconfigure(2, weight=1)
		self.master.columnconfigure(3, weight=1)
		self.master.rowconfigure(0, weight=3)
		self.master.rowconfigure(1, weight=1)
		self.master.rowconfigure(2, weight=1)
		self.master.rowconfigure(3, weight=1)


# Functionality

	# Key Bindings
		master.bind('<Return>', self.search)

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

	# Text Updating
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

################################# MAIN #########################################

if __name__ == "__main__":
	root = tk.Tk()
	checky_app = CheckyGUI(root)
	root.mainloop()