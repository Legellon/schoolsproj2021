import xml.etree.ElementTree as ET
from read import readFromXML_toDict
from dijkstra import dijkstra_XML

locationMap = ET.parse("graph_1.xml")
locationMap_root = locationMap.getroot()

xml_dict = readFromXML_toDict(locationMap_root)

START_POINT = 10
END_POINT = 6

shortest_way = dijkstra_XML(xml_dict, START_POINT, END_POINT, 0)
shortest_distance = dijkstra_XML(xml_dict, START_POINT, END_POINT, 1)

print(shortest_way)
print(shortest_distance)