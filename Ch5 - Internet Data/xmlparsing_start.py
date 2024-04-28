# 
# Example file for parsing and processing XML
# LinkedIn Learning Python course by Joe Marini
#

import xml.dom.minidom

def main():
    # use the parse() function to load and parse an XML file
    doc = xml.dom.minidom.parse("samplexml.xml")
    
    # print out the document node and the name of the first child tag
    print(doc.nodeName)
    print(doc.firstChild.tagName)

    # get a list of XML tags from the document and print each one
    skills = doc.getElementsByTagName("skill")
    print(skills.length, "skills are listed.")
    for i in skills:
        print(i.getAttribute("name"))
      
    # create a new XML tag and add it into the document
    newSkill = doc.createElement("skill")
    newSkill.setAttribute("name","SQL")
    doc.firstChild.appendChild(newSkill)
    
    skills = doc.getElementsByTagName("skill")
    print(skills.length, "skills are listed.")
    for i in skills:
        print(i.getAttribute("name"))


if __name__ == "__main__":
    main()

