import os
import re
from tkinter import *
from tkinter import filedialog

def encoding_dec(initialfile):
    with open(initialfile) as encodeFile:
        first_line = encodeFile.readline()
        encodeFile.close()
        #print(re.search((r'[eE][nN][cC][oO][dD][iI][nN][gG].*'), first_line).group())
        if re.search(r'[iI][sS][oO]-8859.*', first_line) != None:
            return('latin-1')
        else:
            return("utf-8")

def select_files():
    root = Tk()
    fileNames = filedialog.askopenfilenames(parent=root, title="Choose Files", initialdir=os.getcwd(), \
                                                filetypes=(("xml files", "*.xml"), ('all files', "*.*")))
    root.destroy()
    return list(fileNames)

fileNames = select_files()
testList = []
regexPartType = r"(<PartType.*/>)"  # finds PartType based on regex
#regexPartType = r"(<PartNumber.*</PartNumber>)"
#regexDigit = r">.*<"
regexDigit = r'\d+'

for f in range(len(fileNames)):
    with open(fileNames[f],  'r', encoding = encoding_dec(fileNames[f])) as infile:
        read_data = infile.read()
        row = []
        row.append(fileNames[f])
    for i in (re.findall(regexPartType, read_data)):
        if (re.search(regexDigit, i).group()) not in row:
            row.append(re.search(regexDigit, i).group())
    testList.append(row)

i = 0
for x in testList:
    i += 1
    for y in x:
        for x2 in testList[i:]:
            for y2 in x2:
                if y2 == y:
                    print(str(y2) + ' found in ' +
                          str(x[0]).rpartition('/')[-1] + ' and ' + str(x2[0]).rpartition('/')[-1])

input("Hit any key to exit the program. Be careful out there!")