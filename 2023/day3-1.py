import re
my_file = open("input3", "r")
data = my_file.read()




lines=data.split("\n")
lines.pop()
sum=0

linecount=len(lines)

for counter in range(0,linecount):


    symbolposition=[]
    position=0
    for c in lines[counter]:
        position+=1
        if c.isdigit() or c == '.':
            continue
        else:
            symbolposition.append(position-1)

    position=0
    if counter>0:
        for c in lines[counter-1]:
            position+=1
            if c.isdigit() or c == '.':
                continue
            else:
                symbolposition.append(position-1)

    position=0
    if counter<linecount-1:
        for c in lines[counter+1]:
            position+=1
            if c.isdigit() or c == '.':
                continue
            else:
                symbolposition.append(position-1)

    pat = re.compile(r"(\d+)")

    for m in pat.finditer(lines[counter]):
        valid=False

        for position in symbolposition:
            if position >= m.start()-1 and position <= m.end():
                valid=True

        if valid:
            sum+=int(lines[counter][m.start():m.end()])



print(sum)
