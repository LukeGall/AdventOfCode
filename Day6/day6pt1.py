input_file = open("input.txt", "r")
points = input_file.read().split("\n")
points.remove(points[len(points)-1])


iCoords = []
jCoords = []
for point in points:
    newPoint = point.split(", ")
    iCoords.append(int(newPoint[0]))
    jCoords.append(int(newPoint[1]))

maxI = int(max(iCoords))
maxJ = int(max(jCoords))

edgePoints = {}
areaOfPoints = {}
for point in points:
    areaOfPoints[point] = 1
    edgePoints[point] = False


def findClosetPoint(i, j, areaOfPoints, points):
    min = None
    pt = None
    joint = False
    for point in points:
        newPoint = point.split(", ")
        distance = abs(i - int(newPoint[0])) + abs(j - int(newPoint[1]))
        if min is None or distance < min:
            min = distance
            pt = point
            joint = False
        elif distance == min:
            joint = True
    if i == maxI or j == maxJ or i == 0 or j == 0:
        edgePoints[pt] = True
    if not joint:
        areaOfPoints[pt] += 1


for i in range(maxI):
    for j in range(maxJ):
        findClosetPoint(i, j, areaOfPoints, points)


max = 0
maxPt = None
for point in areaOfPoints.keys():
    if not edgePoints[point]:
        if areaOfPoints[point] > max:
            max = areaOfPoints[point]
            maxPt = point

print(max)
print(maxPt)
print(edgePoints[maxPt])
