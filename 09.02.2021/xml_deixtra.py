import xml.etree.ElementTree as ET

pointsTo = [1, 5]
points_routes = [[],[]]

postMap = ET.parse("map.xml")
postMapRoot = postMap.getroot()

for point in postMapRoot[0]:
    points_routes[0].append(point.attrib)

matrix_of_distances = [[0] * len(points_routes[0]) for i in range(len(points_routes[0]))]

for route in postMapRoot[1]:
    points_routes[1].append(route.attrib)
    matrix_of_distances[int(route.attrib['from']) - 1][int(route.attrib['to']) - 1] = int(route.attrib['cfd'])

is_used = [False] * len(points_routes[0])
distances_to_point = [math.inf] * len(points_routes[0])

minimal_distance = 0
minimal_point = pointsTo[0] - 1

distances_to_point[minimal_point] = 0

while minimal_distance < math.inf:
    i = minimal_point
    is_used[i] = True

    near_routes = []
    for route in postMapRoot[1]:
        if(route.attrib['from'] == i): 
            near_points.append(int(point.attrib['to']) - 1)

    for j in near_routes:
        if distances_to_point[i] + matrix_of_distances[i][j] < distances_to_point[j]:
            distances_to_point[j] = distances_to_point[i] + 

    minimal_distance = math.inf

    for i in range(len(points_routes[0])):
        if not used[i] and distances_to_point[i] < minimal_distance:
            minimal_distance = distances_to_point[i]
            minimal_point = i
    
    