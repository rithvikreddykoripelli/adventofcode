f = open("input.txt", "r")
ans = []
max1 = 0
max2 = 0
max3 = 0
count = 0

for line in f:
    if line == '\n':
        if count > max1:   
            max3 = max2
            max2 = max1
            max1 = count
        elif count > max2:
            max3 = max2
            max2 = count
        elif count > max3:
            max3 = count
        ans.append(count)
        count = 0
    else:
        count+=int(line)
print(max1)
print(max2,max3)
print(max1+max2+max3)
