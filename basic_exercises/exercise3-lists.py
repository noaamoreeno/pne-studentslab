temperatures = [15.5, 17.2, 14.8, 16.0, 18.3, 20.1, 19.5]

def avg():
    count = 0
    for temp in temperatures:
        count += temp
    return round(count / len(temperatures), 1)

def higher():
    h = []
    for temp in temperatures:
        if temp > 17:
            h.append(temp)
    return len(h)

def main():
    print("Wednesday:", temperatures[2])
    print("Max:", max(temperatures))
    print("Min:", min(temperatures))
    print("Average:", avg())
    print("Days above 17:", higher())
    print("Sorted:", sorted(temperatures))
main()