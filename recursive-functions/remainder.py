def remainder(dividend,divisor):
    if dividend < divisor:
        return dividend

    else:
        return remainder(dividend-divisor,divisor)


print(remainder(23,7))
    