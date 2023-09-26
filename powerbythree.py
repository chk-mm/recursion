def power_3(number):
    if number == 0:
        return False
    if number == 1:
        return True
    if number%3 == 0:
        return power_3(number//3)
    else:
        return False


print(power_3(6))
print(power_3(27))
