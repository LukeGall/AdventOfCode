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


while inp != removePairs(inp):
    inp = removePairs(inp)

print(len(inp))
