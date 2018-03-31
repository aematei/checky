import checky_functions as cf
from missing import Missing

from tkinter import filedialog
from tkinter import *



 
root = Tk()

missing = Missing()

top_frame = Frame(master=root)

right_frame = Frame(master=root)
bottom_frame = Frame(master=root)

# Left Frame 
left_frame = Frame(master=root)
left_frame.grid(row=1, column=1)

found_text = Text(master=left_frame, state=DISABLED, bg="GREEN")



missing_scrollbar = Scrollbar(master=right_frame, command=missing_text.yview)

missing_text = Text(master=right_frame, state=DISABLED, bg="RED", yscrollcommand=missing_scrollbar.set)
found_text = Text(master=left_frame, state=DISABLED, bg="GREEN")


single_entry = Entry(master=bottom_frame)

search_button = Button(master=bottom_frame, text="Search")
load_missing = Button(master=right_frame, text="Load Missing", command = lambda: cf.get_missing(root, missing, missing_text))
load_batch_found = Button(master=left_frame, text="Load Found")

missing_scrollbar.grid(row=1, column=1, sticky=W)
search_button.grid(row=0, column=0, sticky=S)
single_entry.grid(row=0, column=1)
load_batch_found.grid(row=0, column=0)
found_text.grid(row=1, column=0)
load_missing.grid(row=0, column=1)
missing_text.grid(row=1, column=0)

top_frame.grid(row=0, columnspan=2)

right_frame.grid(row=1, column=2)
bottom_frame.grid(row=2, columnspan=2)



root.mainloop()