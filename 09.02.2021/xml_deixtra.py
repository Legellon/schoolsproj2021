import xml.etree.ElementTree as ET
import math

postMap = ET.parse("map.xml")
postMapRoot = postMap.getroot()

pointsWithRoutes = {}

for point in postMapRoot[0]:
    prop = {'x': float(point.attrib['x']), 'y': float(point.attrib['y'])}

    pointsWithRoutes.update({point.attrib['id']: {'prop': prop, 'routes': []} })

COUNT_OF_POINTS = len(pointsWithRoutes.keys())

matrixOfWeights = [[0] * COUNT_OF_POINTS for currentPoint in range(COUNT_OF_POINTS)]

for route in postMapRoot[1]:
    _distance = math.sqrt(pow(pointsWithRoutes[route.attrib['from']]['prop']['x'] - pointsWithRoutes[route.attrib['to']]['prop']['x'], 2) + pow(pointsWithRoutes[route.attrib['from']]['prop']['y'] - pointsWithRoutes[route.attrib['to']]['prop']['y'], 2))
    _vmax = float(route.attrib['vmax'])

    new_route = {'to': route.attrib['to'], 'weight': _distance / _vmax}
    pointsWithRoutes[route.attrib['from']]['routes'].append(new_route)

    matrixOfWeights[int(route.attrib['from'])-1][int(route.attrib['to'])-1] = new_route['weight']

used_point = [False] * COUNT_OF_POINTS
distance = [math.inf] * COUNT_OF_POINTS
previous_point = [None] * COUNT_OF_POINTS
path_fromStart = []

START_POINT = 8
END_POINT = 1

minimal_distance = 0
minimal_point = START_POINT - 1

distance[minimal_point] = 0

while minimal_distance < math.inf:
    currentPoint = minimal_point
    used_point[currentPoint] = True

    for near_availablePoint in pointsWithRoutes[str(currentPoint + 1)]['routes']:
        near_availablePoint = int(near_availablePoint['to']) - 1

        if distance[currentPoint] + matrixOfWeights[currentPoint][near_availablePoint] < distance[near_availablePoint]:
            distance[near_availablePoint] = distance[currentPoint] + matrixOfWeights[currentPoint][near_availablePoint]

            previous_point[near_availablePoint] = currentPoint + 1

    minimal_distance = math.inf

    for currentPoint in range(COUNT_OF_POINTS):
        if not used_point[currentPoint] and distance[currentPoint] < minimal_distance:
            minimal_distance = distance[currentPoint]
            minimal_point = currentPoint

while END_POINT is not None:
    path_fromStart.insert(0, END_POINT)
    END_POINT = previous_point[END_POINT - 1]

print(distance)
print(path_fromStart)
#print(path_fromStart)