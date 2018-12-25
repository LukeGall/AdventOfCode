input_file = open("input.txt", "r")
lines = input_file.read().split("\n")
lines.remove("")

steps = {}
runableSteps = []
order = []
for line in lines:
    parts = line.split()
    fPt = parts[1]
    sPt = parts[7]
    if sPt not in steps.keys():
        steps[sPt] = []
    if fPt not in steps.keys():
        steps[fPt] = []
    steps[sPt] += fPt


def nextStep():
    for key in steps.keys():
        if steps[key] == [] and key not in runableSteps:
            runableSteps.append(key)
    runableSteps.sort(reverse=True)
    k = runableSteps.pop()
    del steps[k]
    return k


def runStep(step):
    order.append(step)
    if step != "":
        for key in steps.keys():
            if step in steps[key]:
                steps[key].remove(step)


while len(steps) != 0:
    runStep(nextStep())
print(''.join(order))
