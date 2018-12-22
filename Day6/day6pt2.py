input_file = open("input.txt", "r")
points = input_file.read().split("\n")
points.remove(points[len(points)-1])

maxI = 500
maxJ = 500

edgePoints = set()
areaOfPoints = {}
areaOfPoints["0"] = 0
for point in points:
    areaOfPoints[point] = 0


def findClosetPoint(i, j):
    min = None
    pt = None
    joint = False
    for point in points:
        newPoint = point.split(", ")
        distance = abs(int(newPoint[0]) - i) + abs(int(newPoint[1]) - j)
        if min is None or distance < min:
            min = distance
            pt = point
            joint = False
        elif distance == min:
            min = distance
            joint = True
    if not joint:
        return pt
    else:
        return "0"


for i in range(maxI):
    edgePoints.add(findClosetPoint(i, 0))
    if findClosetPoint(i, 0) == '5, 5':
        print(i, 0)
    edgePoints.add(findClosetPoint(i, maxJ))
    if findClosetPoint(i, maxJ) == '5, 5':
        print(i, maxJ)

for j in range(maxJ):
    edgePoints.add(findClosetPoint(0, j))
    if findClosetPoint(0, j) == '5, 5':
        print(0, j)
    edgePoints.add(findClosetPoint(maxI, j))
    if findClosetPoint(maxI, j) == '5, 5':
        print(maxI, j)

for i in range(maxI):
    for j in range(maxJ):
        areaOfPoints[findClosetPoint(i, j)] += 1


max = 0
maxPt = None
for point in areaOfPoints.keys():
    if point not in edgePoints:
        if areaOfPoints[point] > max:
            max = areaOfPoints[point]
            maxPt = point

print(max)
print(maxPt)
