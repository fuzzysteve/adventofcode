import re
my_file = open("input4", "r")

data = my_file.read()


lines=data.split("\n")
lines.pop()


score=0
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
    if gamewins>0:
        score+=pow(2,gamewins-1)



print(score)
