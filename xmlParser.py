#convert the Gates file to UTF-8 using notepad. Seems then run this program to export valid file.
#Seems Gates does not know how XML files work, or standards....

i = 0
ultLine = ""
path = "C:\Automate Data\Test ACE & PIE\MAMDocument78506.html"
output = "C:\\Automate Data\\TestOut.txt"

regexTable = r''
tableHeader = '<tr><td width="15%"><font color="black" face="verdana"><b>Part Number</b></font></td><td width="15%"><font color="black" face="verdana"><b>Part Type</b></font></td><td width="30%"><font color="black" face="verdana"><b>Part Description</b></font></td><td width="10%"><font color="black" face="verdana"><b>LIVE Total</b></font></td><td width="10%"><font color="black" face="verdana"><b>TEST Total</b></font></td><td width="15%"><font color="black" face="verdana"><b>Tolerance</b></font></td><td width="5%"><font color="black" face="verdana"><b>Pies</b></font></td></tr>'
from bs4 import BeautifulSoup
print(path)
with open(path, 'r') as infile:
    read_data = infile.read()
soup = BeautifulSoup(read_data, 'html.parser')
#print(soup.prettify())


importantTable = (soup.findAll('tr'))
# for i in soup.findAll('table')[2]:
#     print(i.findAll('td'))
    #print(i)

#print(importantTable)
for i in importantTable:
    print(i)

#print(revisedList)
# tr_tag = soup.tr
# # print(tr_tag.contents)
# # for child in tr_tag.descendants:
# #     print(child)
# for parent in tr_tag.parents:
#     if parent is None:
#         print(parent)
#     else:
#         print(parent.name)

# for tr in soup.findAll("table")[2]:
#     for td in tr.findAll('tbody'):
#         if not td.attrs.get('style'):
#             print (td)
# rows = importantTable.findAll('tr')
#
# for row in rows:
#     cols=row.find_all('td')
#     cols=[x.text.strip() for x in cols]
#     print (cols)

# for row in rows:
#     cells = row.findChildren('td')
#     for cell in cells:
#         value = cell.string
#         print("The value in this cell is %s" % value)

# print(importantTable)
# tableSoup = BeautifulSoup(importantTable, 'html.parser')
# print(tableSoup.prettify())


#     c = infile.read(1)
#     if not c:
#         print("End of file")
#         break
#     print("Read a character:", c)
# abocve code is to byte read characters, not used but good to have

# output = open(output, 'w')
# print(infile)
#
# print(soup.prettify())
# output.write(soup.prettify())
# output.close()
# infile.close()

#contents = infile.read()

# app_tag = soup.find('app')
# app_tags= soup.find_all('app')
# for i in range(app_tags):
#     print(app_tag.contents)

# import xml.etree.ElementTree
# from xml.dom import minidom
# mydoc = minidom.parse(path)
# #tree = ET.parse(path)
# #e = xml.etree.ElementTree.parse(path).getroot()
# print(mydoc)
# #threadSoup = BeautifulSoup(mydoc)
# #print(mydoc.prettify())
#
# items = mydoc.getElementsByTagName('PartType')
# print('Item #2 attribute:')
# print(items)
# print(items[1].attributes["name"].value)

# import xml.etree.ElementTree as ET
# tree = ET.parse(path)
# root = tree.getroot()
#
# # one specific item attribute
# print('Item #2 attribute:')
# print(root[0][1].attrib)
#
# # all item attributes
# print('\nAll attributes:')
# for elem in root:
#     for subelem in elem:
#         print(subelem.attrib)
#
# # one specific item's data
# print('\nItem #2 data:')
# print(root[0][1].text)
#
# # all items data
# print('\nAll item data:')
# for elem in root:
#     for subelem in elem:
#         print(subelem.text)