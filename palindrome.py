def palindrome(arr):
    if len(arr) < 2:
        return True
    if arr[-1] == arr[0]:
        return palindrome(arr[1:len(arr)-1])
    else:
        return False

arr = 'oo'


print(palindrome(arr))
