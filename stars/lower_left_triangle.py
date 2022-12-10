# lower left triangle

x = 1
n = 5
while x<=n:
    j=n
    while j>=x:
        print("*", end = " ")
        j-= 1
    print()
    x+=1
