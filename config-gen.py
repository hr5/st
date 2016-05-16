import sys

def getColorNumber(string):
    digitString = None

    digitPos = -1
    for i, val in enumerate(string):
        if val.isdigit():
            digitPos = i;
            break

    if digitPos == -1:
        return digitString

    digitString = ""

    while digitPos < len(string) and string[digitPos].isdigit():
        digitString += string[digitPos]
        digitPos += 1

    return int(digitString)

def getColorCode(string):
    colorCode = None

    colorPos = string.find("#")
    if colorPos == -1:
        return colorCode

    colorCode = "#"
    colorPos += 1
    while colorPos < len(string) and string[colorPos].isprintable():
        colorCode += string[colorPos]
        colorPos += 1

    return colorCode

if (len(sys.argv) < 2):
    sys.stderr.write("A input filename is required\n")
    exit(1)

FILENAME = sys.argv[1]
template = open("config.h.template", "r").read();

colors = []
for x in range(16):
    colors.append("#000000")

file = open(FILENAME, "r")
for line in file:
    if "color" in line:
        colorIndex = getColorNumber(line)
        colorHex = getColorCode(line)
        colors[colorIndex] = colorHex

for i in range(16):
    s = "%COLOR" + str(i) + "%"
    template = template.replace(s, colors[i])

with open("config.h", "w") as outputFile:
    outputFile.write(template)
