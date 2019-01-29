import os
from tkinter import *
from tkinter import filedialog
from bs4 import BeautifulSoup
def select_files():
    root = Tk()
    fileNames = filedialog.askopenfilename(parent=root, title="Choose Files", initialdir=os.getcwd(), \
                                            filetypes=(("xml files", "*.xml"), ('all files', "*.*")))
    root.destroy()
    return (fileNames)

def save_dest():
    root = Tk()
    filename = filedialog.asksaveasfilename(initialdir=os.getcwd(), defaultextension=('.xml'), \
                                            title="Select files",
                                            filetypes=(("xml files", "*.xml"), ('all files', "*.*")))
    root.destroy()
    return filename

with open(select_files(), 'r') as infile:
    read_data = infile.read()
soup = BeautifulSoup(read_data, 'lxml')

outfile = save_dest()
line = soup.prettify()
with open(outfile, 'w') as out:
    out.write(soup.prettify())