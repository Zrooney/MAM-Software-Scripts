import os
import re
from tkinter import *
from tkinter import filedialog

# def select_files():
#     root = Tk()
#     fileNames = filedialog.askopenfilenames(parent=root, title="Choose Files", initialdir=os.getcwd(), \
#                                                 filetypes=(("xml files", "*.xml"), ('all files', "*.*")))
#     root.destroy()
#     return list(fileNames)
#
# def save_dest(defaultFileName=''):
#     root = Tk()
#     filename = filedialog.asksaveasfilename(initialdir=os.getcwd(), defaultextension=('.xml'), \
#                                             title="Select files", initialfile=defaultFileName,
#                                             filetypes=(("xml files", "*.xml"), ('all files', "*.*")))
#     root.destroy()
#     return filename
#fileNames = select_files()
#testList = []

importantBits = ["Spectra", "O'Reilly Private Label", "O'Reilly Private Label	O'Reilly - Masterpro - Spectra	Spectra"]
fileName = "Spect-O'Reilly - OPI (MasterPro)-OriginalACES-SpectraPremiumIndustries_Masterpro(ACES)_10102018_135216.zip" #always starts with 5 letter master brand, then sub brand (not char limited), then product line
brandCode = "ORCW"
print(str(importantBits[0])[:5]) #first 5 char of string at index 0
print(str(importantBits[1]).split((" "))[0])
if (fileName.find(str(importantBits[0])[:5])) != -1:
    if fileName.find(str(importantBits[1]).split((" "))[0]) != -1:
        print("you found it")

# regex = r"(<AssetName>^[A-Za-z0-9_-]*$</AssetName>)"
#matches = re.findall(regex3, read_data)
# outFile = ""
# for i in range(len((matches))):
#     matches[i] = matches[i] + ".jpg</AssetName>"
# # print("Full match: %s" % (matches[i]))
# print("The thinking box is thinking....very hard")
# outFile = re.sub(regex2, lambda match: matches.pop(0), read_data, count=len(matches))
# # outFile = re.sub(regex2, matches[i], read_data)
# outputRaw = save_dest(defaultName)
# with open(outputRaw, 'w') as output:
#     output.write(outFile)
# output.close()


# from ftplib import FTP
# #ftp = FTP(user = 'mamuser', passwd = 'dGVjaG4wbDBnaWVzISE', source_address= ("amazon.openwebs.com", 22))
# ftp = FTP('ftp.debian.org',)
# ftp.login()
# print(ftp.pwd())
# #ftp.retrlines('NLST')
# #ftp.pwd()
# #print(ftp)
#
# #print(ftp.getwelcome())






















#-------Code for XMLFileJoiner

# from bs4 import BeautifulSoup
# import os
# import re
# import itertools
#
# #path = "C:\Automate Data\Test ACE & PIE\KST20180920_ACESV3.xml"
#
#
#
#
# from tkinter import *
# from tkinter import filedialog
#
# def select_files():
# 	root = Tk()
# 	root.filename = filedialog.askopenfilename(parent = root,title = "Choose Files", initialdir = os.getcwd())
# 	# rootdir = (root.filename)
# 	# root.destroy()
# 	# outList = list(rootdir)
# 	return (root.filename)
#
# def save_dest(defaultFileName = ''):
# 	root = Tk()
# 	filename = filedialog.asksaveasfilename(initialdir = os.getcwd(),defaultextension = ('.xml'),  \
# 											title = "Select files", initialfile = defaultFileName,
# 											filetypes = (("xml files" , "*.xml"),('all files', "*.*")))
# 	root.destroy()
# 	return filename
#
#
# def rawcount(filename):
# 	f = open(filename, 'rb')
# 	lines = 0
# 	buf_size = 1024 * 1024
# 	read_f = f.read
#
# 	buf = read_f(buf_size)
# 	while buf:
# 		lines += buf.count(b'\n')
# 		buf = read_f(buf_size)
# 	return lines
#
#
#
# path  = 'C:\Automate Data\Test ACE & PIE\Carter Fuel Systems_Import Direct Fuel ACES_2018-09-20_FULL.xml'
# #path = 'C:\Automate Data\Test ACE & PIE\KST20180920_ACESV3.xml'
# file = 'C:\Automate Data\Test ACE & PIE\LINES REMOVES.xml'
# counter = 2
# #outputfile = file
# #(.*)|
# regexDecider = r'<[fF]ooter>\s'
# #regexHeader = r'<?[xXmMlL]([\S\s])*</[hH]eader>'
# regexHeader = r'<\?[xXmMlL][\s\S]*</[hH]eader>'
# regexFooter = r'<[fF]ooter[\s\S]*</[aA][cC][eE][sS]>'
#
# # regexFooterSpace = r'<Footer>' \
# # 			  r'\s*' \
# # 			  r'.*' \
# # 			  r'\s*' \
# # 			  r'\</Footer>' \
# # 			  r'\s*' \
# # 			  r'\</ACES>'
# regexFooterOneLine = r''
# regexXMLVersion = r''
# regexRecordCount = r'\d+'
# #regexApp = r'App action="A" id="10"'
# regexApp = r'<[aA][pP][pP] [aA]ction=\W\w\W [iI][dD]=[\'\"]\d*[\'\"]'
# regexAppReplace = r'<[aA][pP][pP] [aA]ction=\W\w\W [iI][dD]=[\'\"]?'
# with open(path, 'r') as infile:
# 	read_data = infile.read()
# matches = (re.findall(regexFooter, read_data))
# appID = (re.findall(regexAppReplace, read_data))
#
# if (re.search(regexHeader, read_data)) == None:
# 	print('Nothing Found, files fucked')
# else:
# 	print("file is formatted correctly")
#
# #totalCount = int(re.search(regexRecordCount, matches[0]).group())
# #print(int(re.search(regexRecordCount,re.search(regexFooter, read_data).group()).group()))
# print(appID)
# #print(totalCount)
# for i in range(len((appID))):
# 	#matches[i] = matches[i] + ".jpg</AssetName>"
# 	appID[i] = appID[i] + str( i + int(re.search(regexRecordCount, re.search(regexFooter, read_data).group()).group())) + '\"'
# 	#print("Full match: %s" % (appID[i]))
#
# with open(file, 'w') as outfile:
# 	#for fname in filenames:
# 	with open(path, 'r') as infile:
# 		read_data = infile.read()
# 		outFile = re.sub(regexApp, lambda match: appID.pop(0), read_data, count=len(appID))
# 		#read_data3 = re.sub(regexFooter, "", read_data2)
# 		#read_data2 = re.sub(regexHeader, "", read_data2)
# 		#read_data3 = read_data3 + "\n<Footer>\n<RecordCount>" + str(1) +"<RecordCount>\n</Footer>\n</ACES>"
# 		outfile.write(outFile)
#
#
#
#
#
#
#
#
# # path = select_files()
# # defaultName =  os.path.basename(os.path.normpath(path))
# #
# # with open(path, 'r') as infile:
# #     read_data = infile.read()
# #
# # regex3 = r"</.*>" #Finds anything, drops the last character as its usually a special character
# # regex2 = r"(<[aA]sset[nN]ame>.*\.*</[aA]sset[nN]ame>)" #Finds anything, includes the AssetName tag
# # regex = r"(<AssetName>\w+|d+\D+</AssetName>)" #finds anything without file extension
# # #regex = r"(<AssetName>^[A-Za-z0-9_-]*$</AssetName>)"
# # matches = re.findall(regex3, read_data)
# #
# # outFile = ""
# # for i in range(len((matches))):
# # 	#matches[i] = matches[i] + ".jpg</AssetName>"
# # 	print("Full match: %s" % (matches[i]))
# # print("The thinking box is thinking....very hard")
# #
# # outFile = re.sub(regex3, r'\1\n', read_data)
# # #outFile = re.sub(regex2, matches[i], read_data)
# # outputRaw = save_dest(defaultName)
# # with open(outputRaw, 'w') as output:
# #     output.write(outFile)
# # output.close()
#
# # with open(path) as infile:
# #     read_data = infile.read()
# # #print(read_data)
# # soup = BeautifulSoup(read_data,'lxml')
# # #print(soup)
# # tag = soup.enginebase
# # #print(soup.prettify())
# #
# # print(tag)
# # list = soup.find_all('enginebase', 'id')
# # for tag in soup.find_all(re.compile('enginebase')):
# #     #print(tag.name)
# #
# #     print(tag['id'])
# #     # print(i)
# #     # tag = soup.enginebase
# #     # #print(tag.attrs)
# #
# # #print(soup.prettify())