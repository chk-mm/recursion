def findmax(arr):
    if len(arr) == 1:
        return arr[0]
    last = arr[-1]
    rest = arr[:len(arr)-1]
    if last > findmax(rest):
        return last
    else:
        return findmax(rest)

arr = [3,7,8,10,9,5,11,2,1,2,333,20]


print(findmax(arr))