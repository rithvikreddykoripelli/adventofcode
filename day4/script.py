f = open("input.txt", "r")

ans1 = 0
ans2 = 0
for line in f:
    line = line.strip()
    r1,r2 = line.split(",")
    a,b = map(int,r1.split("-") )
    x,y = map(int,r2.split("-"))
    # if x <= a and y <=b and y >=a and :
    #     print(x,y,a,b)
    #     ans1+=1
    # elif a <= x and b <=y and b>=x and a <=y:
    #     print(x,y,a,b)
    #     ans1+=1
    if a <=x and a<=y and  x<=b and y<=b:
        ans1+=1
    elif x <= a and x<=b and a<=y and b<=y:
        ans1+=1

    if a<=x and x <=b:
        print(a,b,x,y)
        ans2+=1
    elif x<=a and a<=y:
        print(a,b,x,y)
        ans2+=1
    
print(ans1)
print(ans2)



# a x y b

# x a b y 

# a x b y || a x y b
# x a y b || x a b y

