# convert the Gates file to UTF-8 using notepad. Seems then run this program to export valid file.
# Seems Gates does not know how XML files work, or standards....
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import filedialog
import os

def select_files():
	root = Tk()
	root.filename = filedialog.askopenfilenames(parent = root,title = "Choose Files", initialdir = os.getcwd())
	rootdir = (root.filename)
	root.destroy()
	outList = list(rootdir )
	return (outList)

def save_dest():
	root = Tk()
	filename = filedialog.asksaveasfilename(initialdir = os.getcwd(),defaultextension = ('.xml'),  \
											title = "Select files", filetypes = (("xml files" , "*.xml"),('all files', "*.*")))
	root.destroy()
	return filename

i = 0
ultLine = ""
path = "C:\\Automate Data\\CopiedGates.txt"
output = "C:\\Automate Data\\TestOut.xml"
print(path)

with open(path, 'rb') as infile:
    output = open(output, 'w', encoding='utf8')
    for line in infile:
        ultLine += line
        i = 1 + i
        print(i)

print(ultLine)
print("Processing..... Might take a while.")
soup = BeautifulSoup(ultLine, 'xml')
output.write(soup.prettify())
infile.close()
output.close()
# while True:
#     c = infile.read(1)
#     if not c:
#         print("End of file")
#         break
#     print("Read a character:", c)
# abocve code is to byte read characters, not used but good to have


#IMPROVEMENTS:
#Last item tag, </items> needs to be added
# get rid of erronous 'xml' tag