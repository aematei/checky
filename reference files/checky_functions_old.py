import csv

from tkinter import filedialog
from tkinter import *

def populate(filename):
    """ 
    Takes a barcode vs. description csv file and
    populates a dictionary as {barcode: description}
    """
    reader = csv.DictReader(open(str(filename)))
    result = {}
    for row in reader:
        for column, value in row.items():
            result.setdefault(column, []).append(value.rstrip())
    dictionary = dict(zip(result['Barcode'], result['Description']))
    return(dictionary)

def get_missing(root, missing, missing_text):
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select file",
        filetypes = (("csv files","*.csv"),("all files","*.*")))
    missing.dictionary = populate(filename)
    missing_text.config(state=NORMAL)
    for barcode, description in missing.dictionary.items():
        missing_text.insert(INSERT, barcode + ':' + description + '\n')
    missing_text.config(state=DISABLED)
    root.update()



