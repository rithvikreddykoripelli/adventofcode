import re

f = open("input.txt", "r")
input_array = f.readlines()
stacks = [[] for x in range(9) ]
stacks2 = [[] for x in range(9) ]


count = 0
for line in input_array[:8]:
    for i in range(9):
        if line[(i*4)+1].strip() != '':
            stacks[i].insert(0,  (line[(i*4)+1]))
            stacks2[i].insert(0, (line[(i*4)+1]))

for line in input_array[10:]:
    num, from_s ,to_s = map(int,re.findall(r'\d{1,3}', line))
    for _ in range(num):
        stacks[to_s-1].append(stacks[from_s-1].pop())
    stacks2[to_s-1] = stacks2[to_s-1] + stacks2[from_s-1][num*-1::]
    for _ in range(num):
        stacks2[from_s-1].pop()

ans1 = ""
ans2 = ""
for stack in stacks:
    ans1+=stack[-1]
for stack in stacks2:
    ans2+=stack[-1]

print(ans1)
print(ans2)

    
