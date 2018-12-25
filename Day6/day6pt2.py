input_file = open("input.txt", "r")
points = input_file.read().split("\n")
points.remove(points[len(points)-1])

maxI = 500
maxJ = 500


def withinRegion(i, j):
    sum = 0
    for point in points:
        newPoint = point.split(", ")
        distance = abs(int(newPoint[0]) - i) + abs(int(newPoint[1]) - j)
        sum += distance
        if sum >= 10000:
            return False
    return True


areaOfRegion = 0
for i in range(maxI):
    for j in range(maxJ):
        if withinRegion(i, j):
            areaOfRegion += 1
print(areaOfRegion)
