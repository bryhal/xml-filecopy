# get a list of xml files

import os
from xml.dom.minidom import parseString
from string import count

def get_file_list(xmlfile):
    file_list = []
    xml = open(xmlfile, "r")
    dom = parseString(xml.read())
    xml.close()
    nodelist = dom.getElementsByTagName("NexJobFileUpload")
    for node in nodelist:
        #print node.toxml()
        #file_list.append(node.toxml())
        file_list.append(str(node.firstChild.nodeValue))
    return file_list

xmlfiles = []

os.chdir("xml")
for files in os.listdir("."):
    if files.endswith(".xml"):
        #print files
        xmlfiles.append(files)

#print xmlfiles
pdffiles = []
for f in xmlfiles:
    #files = get_file_list(f)
    pdffiles.append(get_file_list(f))

# this will be a list of lists
print pdffiles
print len(pdffiles)


# I need a flat list
import itertools

new_list = list(itertools.chain.from_iterable(pdffiles))
print new_list
print len(new_list)





