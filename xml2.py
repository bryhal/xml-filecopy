# get a list of xml files

import os
from xml.dom.minidom import parseString
from string import count
import itertools
import shutil

# define some stuff..
xml_dir = '/Users/bryhal/Documents/workspace/xml-filecopy/xml-filecopy/xml/'         #Path to the XML files
xml_dest = '/Users/bryhal/Documents/workspace/xml-filecopy/xml-filecopy/done_xml/'        #Path to the destination of xmls after processing
file_dir =  '/Users/bryhal/Documents/workspace/xml-filecopy/xml-filecopy/pdf_src/'        #Path to the xml files
file_dest = '/Users/bryhal/Documents/workspace/xml-filecopy/xml-filecopy/pdf_dest/'        #Path to destination directory for pdf files


# Get a list of xml files in xml_dir
def get_xml_file_list(xml_dir):
    xmlfiles = []
    for files in os.listdir(xml_dir):
        if files.endswith(".xml"):
            xmlfiles.append(files)
    return xmlfiles


# Get a list of PDF files referenced in a single xml file
def get_pdf_file_list(xml_file):
    pdf_file_list = []
    xml = open(xml_file, "r")
    dom = parseString(xml.read())
    xml.close()
    nodelist = dom.getElementsByTagName("NexJobFileUpload")
    for node in nodelist:
        # list of basename of files specified in single xml file
        pdf_file_list.append(os.path.basename(str(node.firstChild.nodeValue)))
    return pdf_file_list


def main():    
    # get the list of xml files
    xml_files = get_xml_file_list(xml_dir)
    #print xml_files
    
    # get the list of pdf files from the xml files
    pdf_files = []
    for xml_file in xml_files:
        full_xml_path = xml_dir+xml_file
        pdf_files.append(get_pdf_file_list(full_xml_path))
    
    # this will be a list of lists of pdf basenames 
    #print pdf_files
    
    pdfs_to_copy = list(itertools.chain.from_iterable(pdf_files))
    
    #flattened list of PDF files
    #print pdfs_to_copy
    
    #copy pdf files from src to dest
    for pdf in pdfs_to_copy:
        shutil.copy(file_dir+pdf, file_dest+pdf)
        if os.path.isfile (file_dest+pdf): print "%s %s" %  ('Copied', pdf)
    
    # move xmls to destination
    for xml_file in xml_files:
        shutil.move(xml_dir+xml_file, xml_dest+xml_file)



if __name__ == '__main__':
    main()


'''    
    
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

'''



