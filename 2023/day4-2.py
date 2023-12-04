import re
my_file = open("input4", "r")
#my_file = open("test4", "r")

data = my_file.read()


lines=data.split("\n")
lines.pop()


multipliers=[1 for x in range(len(lines))]

currentline=0
for line in lines:
    line=' '.join(line.split())
    game,setstring=line.split(":")
    winnumbers,mynumbers=setstring.split("|")
    winningnumbers=winnumbers.strip().split(" ")
    mynumbers=mynumbers.strip().split(" ")
    gamewins=0
    for number in mynumbers:
        if number in winningnumbers:
            gamewins+=1
    for x in range(1,gamewins+1):
        if (currentline+x)<len(lines):
            multipliers[currentline+x]+=1*multipliers[currentline]
    currentline+=1

print(sum(multipliers))
