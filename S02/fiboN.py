def fibon(n):
    a, b = 0, 1
    for i in range(n):
        a = a + b
        b = a - b
    return a

print("The 5th fibonacci term:", fibon(5))
print("The 10th fibonacci term:", fibon(10))
print("The 15th fibonacci term:", fibon(15))
