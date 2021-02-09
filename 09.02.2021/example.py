import xml.etree.ElementTree as ET

i = 0

for event, elem in ET.iterparse("locations.xml"):
    i += 1

print(i)