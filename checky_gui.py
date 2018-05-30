import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk

from checky import Checky


class CheckyGUI():
	def __init__(self, master, *args, **kwargs):

# Colors
		self.bg_tan = '#e5e1da'
		self.bg_green = '#f7fff7'
		self.bg_red = '#fff7f7'

# Widgets 

	# Main Frame
		self.master = master
		self.master.minsize(330, 150)
		self.master.withdraw()
		self.master.after(0 ,self.master.deiconify)

		self.checky_style = ttk.Style()
		self.checky_style.configure('found.Treeview', fieldbackground=self.bg_green)
		self.checky_style.configure('missing.Treeview', fieldbackground=self.bg_red)

	# !!!Sub Frames!!!

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
		self.save_menu = tk.Menu(self.filemenu, tearoff=0)
		self.filemenu.add_command(label="New Session", command=self.new_session)
		self.save_menu.add_command(label="Save Found", command=self.save_found)
		self.save_menu.add_command(label="Save Missing",
			command=self.save_missing)
		self.save_menu.add_command(label="Save Both", command=self.save_both)
		
		self.menubar.add_cascade(label="File", menu=self.filemenu)
		self.filemenu.add_cascade(label="Save", menu=self.save_menu)
		
		self.master.config(menu=self.menubar)

	# !!!Text Widgets!!!
		self.default_column_width = 485
		self.load_batch_found = tk.Button(master=self.load_frame_left,
			text="Load Found", command=self.load_batch_found_file)
		
		#!!!
		self.found_text = ttk.Treeview(master=self.text_frame_left, height=50, padding=5, style='found.Treeview')

		self.found_text["columns"] = ("1")
		self.found_text.column("#0", minwidth=70, width=120)
		self.found_text.column("#1", minwidth=70, width=self.default_column_width)
		self.found_text.heading("#0", text="Barcode")
		self.found_text.heading("#1", text="Description")




		self.load_missing = tk.Button(master=self.load_frame_right,
			text="Load Missing", command=self.load_missing_file)
		
		#!!!
		self.missing_text = ttk.Treeview(master=self.text_frame_right, height=50, padding=5)

		self.missing_text["columns"] = ("1")
		self.missing_text.column("#0", minwidth=70, width=120)
		self.missing_text.column("#1", minwidth=70, width=self.default_column_width)
		self.missing_text.heading("#0", text="Barcode")
		self.missing_text.heading("#1", text="Description")


		self.y_scroll_right.config(command=self.missing_text.yview)
		self.x_scroll_right.config(command=self.missing_text.xview)
		self.missing_text.configure(xscrollcommand=self.x_scroll_right.set)
		self.missing_text.configure(yscrollcommand=self.y_scroll_right.set)


		self.y_scroll_left.config(command=self.found_text.yview)
		self.x_scroll_left.config(command=self.found_text.xview)
		self.found_text.configure(xscrollcommand=self.x_scroll_left.set)
		self.found_text.configure(yscrollcommand=self.y_scroll_left.set)
		
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

	# Top Frame Styling

		self.master["bg"] = self.bg_tan
		self.top_frame.config(bg=self.bg_tan)
		self.load_frame_left.config(bg=self.bg_tan)
		self.load_frame_right.config(bg=self.bg_tan)
		self.bottom_frame.config(bg=self.bg_tan)

	# !!!Text Frames Styling!!!



		self.load_frame_left.config(bg=self.bg_tan)
		self.load_frame_right.config(bg=self.bg_tan)
		self.load_batch_found.config(bg=self.bg_tan, highlightthickness=0,
			highlightbackground=self.bg_tan)
#		self.found_text.config(relief="sunken", bg=self.bg_green,
#			highlightbackground=self.bg_green)
		self.load_missing.config(bg=self.bg_tan, highlightthickness=0,
			highlightbackground=self.bg_tan)
#		self.missing_text.config(bg=self.bg_red,
#			highlightbackground=self.bg_red)

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
		self.missing_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
		
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
		for barcode in self.found_text.get_children():
			self.found_text.delete(barcode)
		for barcode, description in self.checky.found.data.items():
			self.found_text.insert("", 0, text=barcode, values=('"'+description)+'"')
	
	def update_missing_text(self):
		"""Updates the 'missing' data text field."""
		for barcode in self.missing_text.get_children():
			self.missing_text.delete(barcode)
		for barcode, description in self.checky.missing.data.items():
			self.missing_text.insert("", 0, text=barcode, values=('"'+description+'"'))



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

	# Menubar Functions
	def new_session(self):
		self.close_save()		
		self.checky = Checky()
		self.update_last_entry('')
		self.update_text()

	def save_missing(self):
		filename = fd.asksaveasfilename(title="Save Missing Barcodes")
		self.checky.save_missing(filename)
		try:
			self.exit_close_save()
		except AttributeError:
			None

	def save_found(self):
		filename = fd.asksaveasfilename(title="Save Found Barcodes")
		self.checky.save_found(filename)
		try:
			self.exit_close_save()
		except AttributeError:
			None

	def save_both(self):
		self.save_found()
		self.save_missing()

	def exit_close_save(self):
		self.close.destroy()
		self.close.quit()

	def close_save(self):
		self.close = tk.Toplevel()
		self.close.resizable(False, False)
		self.close.transient([self.master])
		self.close_str = "Do you want to close this session without saving?"
		self.close_label = tk.Label(master=self.close, text=self.close_str)
		self.close_button = tk.Button(master=self.close, text="Don't Save",
			command=self.exit_close_save)
		self.save_found_button = tk.Button(master=self.close, text='Save Found',
			command=self.save_found)
		self.save_missing_button = tk.Button(master=self.close,
			text='Save Missing', command=self.save_missing)
		self.save_both = tk.Button(master=self.close, text='Save Both',
			command=self.save_both)

		self.close_label.pack(side=tk.TOP)
		self.close_button.pack(side=tk.RIGHT)
		self.save_found_button.pack(side=tk.RIGHT)
		self.save_missing_button.pack(side=tk.RIGHT)
		self.save_both.pack(side=tk.RIGHT)
		self.close.mainloop()


		
################################# MAIN #########################################

if __name__ == "__main__":
	root = tk.Tk()
	checky_app = CheckyGUI(root)
	root.mainloop()