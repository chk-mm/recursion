def rabbits(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    elif n==2:
        return 2
    else:
        return rabbits(n-1)+rabbits(n-2)

input = int(input("number:"))
print(rabbits(input))