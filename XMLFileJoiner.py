import os
from tkinter import *
from tkinter import filedialog


def select_files():
    root = Tk()
    fileNames = filedialog.askopenfilenames(parent=root, title="Choose Files", initialdir=os.getcwd(), \
                                            filetypes=(("xml files", "*.xml"), ('all files', "*.*")))
    root.destroy()
    return list(fileNames)


def save_dest(initaldir=os.getcwd()):
    root = Tk()
    filename = filedialog.asksaveasfilename(initialdir=initaldir, defaultextension=('.xml'), \
                                            title="Select files",
                                            filetypes=(("xml files", "*.xml"), ('all files', "*.*")))
    root.destroy()
    return filename


def encoding_dec(initialfile):
    with open(initialfile) as encodeFile:
        first_line = encodeFile.readline()
        encodeFile.close()
        #print(re.search((r'[eE][nN][cC][oO][dD][iI][nN][gG].*'), first_line).group())
        if re.search(r'[iI][sS][oO]-8859.*', first_line) != None:
            return('latin-1')
        else:
            return("utf-8")


def number_replace(appIDList,total):
    lineRep = ""
    i = total + 1
    for z in range(len((appIDList))):
        #line = re.sub(appIDList[z], re.sub(regexRecordCount, str(i), appIDList[z]), lineRep)
        t = re.sub(regexRecordCount, str(i), appIDList[z])
        #print(t)S
        #appIDList[z] = (re.sub(appIDList[z], t, appIDList[z]))
        i = i + 1
    total = total + (
        int(re.search(regexRecordCount, re.search(regexFooter, read_data).group()).group()))
    print(fname.rpartition('/')[-1] + " : Total Applications: " + str((len((appIDList)))))
    lineRep = re.sub(regexAppReplace, lambda match: appIDList.pop(0), read_data, count=len(appIDList))
    lineRep = re.sub(regexFooter, "", lineRep)
    lineRep = re.sub(regexHeader, "", lineRep)
    return([lineRep, total])

filenames = select_files()
file = save_dest(filenames[0])

regexRecordCount = r'\d+'  # finds digits in regex, used to extract count from footer
regexHeader = r'<\?[xX][mM][lL][\s\S]*</[hH]eader>'  # finds header, includes ACES version and all file specific info
regexFooter = r'<[fF]ooter[\s\S]*</[aA][cC][eE][sS]>'  # finds footer
#regexApp = r'<[aA][pP][pP] [aA]ction=\W\w\W [iI][dD]=[\'\"]\d*[\'\"]'  # finds app id without num
regexAppReplace = r'(<[aA][pP][pP].*>)'  # finds app id with num
totalCount = 0
x = 0
i = 0

with open(file, 'w', encoding = encoding_dec(filenames[0])) as outfile:
    for fname in filenames:
        x = x + 1
        with open(fname, encoding = encoding_dec(fname)) as infile:
            if x == 1:
                read_data = ""
                read_data = infile.read()
                totalCount = totalCount + (
                    int(re.search(regexRecordCount, re.search(regexFooter, read_data).group()).group()))
                i = totalCount
                print(fname.rpartition('/')[-1] + " : Total Applications: " + str(totalCount))
                line = re.sub(regexFooter, "", read_data)
                outfile.write(line)
                infile.close()
            elif 1 < x <= (len(filenames)):
                read_data = ""
                i = totalCount
                appID = []
                read_data = infile.read()
                appID = (re.findall(regexAppReplace, read_data))

                tmp = number_replace(appID, i)
                line = tmp[0]
                totalCount = tmp[1]

                if x != (len(filenames)):
                    outfile.write(line)
                else:
                    outfile.write(line + "<Footer>\n<RecordCount>" + str(totalCount) + "</RecordCount>\n</Footer>\n</ACES>")
                infile.close()

input("Hit any button to exit program")
