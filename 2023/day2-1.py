import re
my_file = open("input2", "r")
data = my_file.read()


maximums = {"red":12,"green":13,"blue":14}


lines=data.split("\n")
lines.pop()
sum=0
for line in lines:
    game,setstring=line.split(":")
    sets=setstring.split(";")
    gamere=re.search(r"Game (\d+)",game)
    gameid=int(gamere.group(1))
    goodgame=True
    for set in sets:
        groups=set.split(", ")
        for group in groups:
            number,colour=group.strip().split(" ")
            if maximums[colour]<int(number):
                goodgame=False
    if goodgame:
        sum+=gameid


print(sum)
