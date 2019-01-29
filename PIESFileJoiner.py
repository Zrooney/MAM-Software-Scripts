import os
from tkinter import *
from tkinter import filedialog

def select_files():
    root = Tk()
    fileNames = filedialog.askopenfilenames(parent=root, title="Choose Files", initialdir=os.getcwd(), \
                                            filetypes=(("xml files", "*.xml"), ('all files', "*.*")))
    root.destroy()
    return list(fileNames)

def save_dest():
    root = Tk()
    filename = filedialog.asksaveasfilename(initialdir=os.getcwd(), defaultextension=('.xml'), \
                                            title="Select files",
                                            filetypes=(("xml files", "*.xml"), ('all files', "*.*")))
    root.destroy()
    return filename

filenames = select_files()
file = save_dest()

regexRecordCount = r'\d+'
regexHeader = r'<\?[xX][mM][lL][\s\S]*<Items>'
regexFooter = r'</[iI]tems[\s\S]*</[pP][iI][eE][sS]>'

totalCount = 0
x = 0
i = 0

with open(file, 'w') as outfile:
    for fname in filenames:
        x = x + 1
        with open(fname) as infile:
            if x == 1:
                read_data = ""
                read_data = infile.read()
                totalCount = totalCount + (
                    int(re.search(regexRecordCount, re.search(regexFooter, read_data).group()).group()))
                print(totalCount)
                line = re.sub(regexFooter, "", read_data)
                outfile.write(line)
            elif 1 < x < (len((filenames))):
                read_data = ""
                z = 0
                read_data = infile.read()
                totalCount = totalCount + (
                    int(re.search(regexRecordCount, re.search(regexFooter, read_data).group()).group()))
                print(totalCount)
                line = re.sub(regexFooter, "", read_data)
                line = re.sub(regexHeader, "", line)
                outfile.write(line)
                infile.close()
            elif x == (len((filenames))):
                read_data = ""
                read_data = infile.read()
                totalCount = totalCount + (
                    int(re.search(regexRecordCount, re.search(regexFooter, read_data).group()).group()))
                print(totalCount)
                line = re.sub(regexFooter, "", read_data)
                line = re.sub(regexHeader, "", line)
                outfile.write(
                    line + "</Items>\n<Trailer>\n<ItemCount>" + str(totalCount) + "</ItemCount>\n</Trailer>\n</PIES>")
                infile.close()
garbage = input("Hit any key to exit...")