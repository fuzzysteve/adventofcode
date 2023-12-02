import re
my_file = open("input1", "r")
data = my_file.read()

help_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0',
    'eno': '1',
    'owt': '2',
    'eerht': '3',
    'ruof': '4',
    'evif': '5',
    'xis': '6',
    'neves': '7',
    'thgie': '8',
    'enin': '9',
    'orez': '0'
}

lines=data.split("\n")

sum=0
for line in lines:
    if len(line)==0:
        break
    forward=line
    reverse=line[::-1]
    m = re.search(r"\d", forward)

    firstdigit=m.start()

    m = re.search(r"\d", reverse)
    lastdigit=m.start()

    forwarddigit=forward[firstdigit]
    reversedigit=reverse[lastdigit]

    m= re.search(r"(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)", forward)

    if m:
        pos=m.start()
        if int(pos)<firstdigit:
            forwarddigit=help_dict[m.group(0)]


    m= re.search(r"(enin)|(thgie)|(neves)|(xis)|(evif)|(ruof)|(eerht)|(owt)|(eno)", reverse)

    if m:
        pos=m.start()
        if int(pos)<lastdigit:
            reversedigit=help_dict[m.group(0)]




    sum+=(int(forwarddigit)*10)+int(reversedigit)



print(sum)
