def fibosum(n):
    a, b = 0, 1
    sum = 0
    for i in range(n):
        sum += a
        a = a + b
        b = a - b
    return sum

print("The sum of first 5 fibonacci terms is:", fibosum(5))
print("The sum of first 10 fibonacci terms is:", fibosum(10))