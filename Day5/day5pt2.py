input_file = open("input.txt", "r")
inp = input_file.read().strip()


def removePairs(string):
    pairs = []
    for i in range(len(string)-1):
        fir = string[i]
        sec = string[i+1]
        if (fir == sec.capitalize() or fir.capitalize() == sec) and fir != sec:
            pairs.append(fir+sec)
    for pair in pairs:
        string = string.replace(pair, "")
    return string


def reducePoly(string):
    while string != removePairs(string):
        string = removePairs(string)
    return len(string)


lets = set([c.lower() for c in inp])

print(reducePoly(inp))

print(min([reducePoly(inp.replace(a, '').replace(a.upper(), ''))
           for a in lets]))
