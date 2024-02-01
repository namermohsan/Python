# Parsing XML 
# ------------------------------------------------------------
#This code requires installing the following library
#pip install xmltodict

import xmltodict

stream = open('sample.xml', 'r')

xml = xmltodict.parse(stream.read())

for line in xml['people']['person']:
    print(line)


#Or we can parse xml files using the lxml library
#pip install lxml

from lxml import etree as ET

stream = open('sample.xml', 'r')

xml = ET.parse(stream)

root = xml.getroot()

for e in root:
    #this line will print it as string
    print(ET.tostring(e))
    print('')
    #this line will search for the ID's and prints them
    print(e.get('ID'))

# Sample output:
# b'<person ID="1">\n    <firstName>John</firstName>\n    <lastName>Doe</lastName>\n    <age>30</age>\n    <email>john.doe@example.com</email>\n  </person>\n  '

# 1
# b'<person ID="2">\n    <firstName>Jane</firstName>\n    <lastName>Smith</lastName>\n    <age>25</age>\n    <email>jane.smith@example.com</email>\n  </person>\n'

# 2

# In addition, there is a built-in module in Python, xml.etree.ElementTree,
# that provides a simple and efficient API for parsing and creating XML data. 
# We can import it using the alias ET, like this: import xml.etree.ElementTree as ET. 
# The rest of the previous code will remain the same.

#All The Very Best,
    #Nameer
