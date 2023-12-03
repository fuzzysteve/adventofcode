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
        if c == '*':
            symbolposition.append(position-1)

    pat = re.compile(r"(\d+)")


    for position in symbolposition:
        gear=[]
        for m in pat.finditer(lines[counter]):
            valid=False
            if position >= m.start()-1 and position <= m.end():
                    valid=True
            if valid:
                gear.append(int(lines[counter][m.start():m.end()]))

        if counter>0:
            for m in pat.finditer(lines[counter-1]):
                valid=False
                if position >= m.start()-1 and position <= m.end():
                    valid=True
                if valid:
                    gear.append(int(lines[counter-1][m.start():m.end()]))

        if counter<linecount-1:
            for m in pat.finditer(lines[counter+1]):
                valid=False
                if position >= m.start()-1 and position <= m.end():
                    valid=True
                if valid:
                    gear.append(int(lines[counter+1][m.start():m.end()]))

        print(counter,gear)
        if len(gear)==2:
            sum+=gear[0]*gear[1]

print(sum)
