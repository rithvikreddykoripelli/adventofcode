f = open('input.txt','r')

rock = ['A', 'X']
paper = ['B','Y']
scissors = ['C','Z']


scorer = {
    'rock': 1,
    'paper':2,
    'scissors':3
}

ans1 = 0
ans2 = 0

def printer_1(o):
    if o in rock:
        return "rock"
    elif o in paper:
        return "paper"
    else:
        return "scissors"

for line in f:
    l,m = line.strip().split(" ")
    ans1+= scorer[printer_1(m)]
    if printer_1(l) == printer_1(m):
        ans1+=3
    elif (l == 'A' and m == 'Z') or (l == 'B' and m == 'X') or (l=='C' and m == 'Y'):
        pass
    else:
        ans1+=6

    #PART 2
    if m == 'X':
        pass
    elif m == 'Y':
        ans2+=3
    else:
        ans2+=6
    
    if m == 'Y':
        ans2+= scorer[printer_1(l)]
    elif m == 'Z':
        if l == 'A':
            ans2+=2
        elif l == 'B':
            ans2+=3
        else:
            ans2+=1
    else:
        if l == 'A':
            ans2+=3
        elif l == 'B':
            ans2+=1
        else:
            ans2+=2
    
    
print(ans1) 
print(ans2)