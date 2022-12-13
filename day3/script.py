f = open("input.txt", "r")

def priority_calc(letter):
    if ord(letter) >= 97:
        return ord(letter) - 96
    else:
        return ord(letter) - 38

ans1 = 0
ans2 = 0

count = 0
lines = []
for line in f:
    count+=1
    line = line.strip()
    mid = len(line)/2
    common_letter = list(set(line[:mid]).intersection(set(line[mid:])))[0]
    ans1+= priority_calc(common_letter)
   
    lines.append(line)
    if count %3 == 0:
        common_letter2 = list(set(lines[0]).intersection(set(lines[1])).intersection(set(lines[2])))[0]
        print(common_letter2)
        ans2+= priority_calc(common_letter2)
        lines = []
    
print(ans1)
print(ans2)