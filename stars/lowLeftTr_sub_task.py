# lower left triangle sub task

x = 1
n = 3
while x<=n:
    j=n
    while j>=x:
        print("*", end = " ")
        j-= 1
    print()
    x+=1
