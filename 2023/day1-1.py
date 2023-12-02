my_file = open("input1", "r")
data = my_file.read()


lines=data.split("\n")

sum=0
for line in lines:
   forward=enumerate(line)
   reverse=enumerate(line[::-1])
   for i, c in forward:
       if c.isdigit():
           sum+=(int(c)*10)
           break
   for i, c in reverse:
       if c.isdigit():
           sum+=int(c)
           break
print(sum)
