import os
import re
from tkinter import *
from tkinter import filedialog

def select_files():
	root = Tk()
	root.filename = filedialog.askopenfilename(parent = root,title = "Choose Files", initialdir = os.getcwd())
	# rootdir = (root.filename)
	# root.destroy()
	# outList = list(rootdir)
	return (root.filename)

def save_dest(defaultFileName = ''):
	root = Tk()
	filename = filedialog.asksaveasfilename(initialdir = os.getcwd(),defaultextension = ('.xml'),  \
											title = "Select files", initialfile = defaultFileName,
											filetypes = (("xml files" , "*.xml"),('all files', "*.*")))
	root.destroy()
	return filename

path = select_files()
defaultName = os.path.basename(os.path.normpath(path))

with open(path, 'r') as infile:
    read_data = infile.read()

regex3 = r"(<[aA]sset[nN]ame>[a-zA-Z0-9]*[^\D])" #Finds anything, drops the last character as its usually a special character
regex2 = r"(<[aA]sset[nN]ame>.*\.*</[aA]sset[nN]ame>)" #Finds anything, includes the AssetName tag
regex = r"(<AssetName>\w+|d+\D+</AssetName>)" #finds anything without file extension
#regex = r"(<AssetName>^[A-Za-z0-9_-]*$</AssetName>)"
matches = re.findall(regex3, read_data)
#outFile = ""
for i in range(len((matches))):
	matches[i] = matches[i] + ".jpg</AssetName>"
	#print("Full match: %s" % (matches[i]))
print("The thinking box is thinking....very hard")
outFile = re.sub(regex2, lambda match: matches.pop(0), read_data, count=len(matches))
#outFile = re.sub(regex2, matches[i], read_data)
outputRaw = save_dest(defaultName)
with open(outputRaw, 'w') as output:
    output.write(outFile)
output.close()

# soup = BeautifulSoup(read_data,'lxml')
# #print(soup.prettify())
#
# print(soup.findAll("assetname"))
# for tag in soup.find_all(re.compile('assetname')):
#     print(tag.string)
#     if (tag.string[-4:] == ".tif") or (tag.string[-4:] == ".tif"):
#         tag.string = ''.join(tag.string.split())
#         tag.string = tag.string[:-4]
#         print(tag.string)
#         tag.string = tag.string + ".jpg"
#     elif (tag.string[-4:] == ".JPG") or (tag.string[-4:] == ".jpg"):
#         print("All good boss")
#     else:
#         tag.string = tag.string + ".jpg"
#         print(tag.string)
#     print(tag)




    #print(tag)
    #print(tag['id'])




