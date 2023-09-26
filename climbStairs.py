print_a = []
def climbStairs(n: int) -> int:
    if n == 1:
        return print_a.append('1')
    elif n == 2:
        return print_a.append('2')
    else:
        return climbStairs(n - 1) + climbStairs(n - 2)

climbStairs(3)

print(print_a)