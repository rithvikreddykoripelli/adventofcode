f = open("input.txt", "r")

line = f.readline()

index = 0
while True:
    if len(set(line[index:index+14])) == 14:
        break
    index+=1
print(index+14)



