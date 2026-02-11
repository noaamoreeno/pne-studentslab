def score(score):
    if 8.9 < score <= 10.0:
        letter = "A"
    elif 6.9 < score <= 8.9:
        letter = "B"
    elif 4.9 < score <= 6.9:
        letter = "C"
    elif 2.9 < score <= 4.9:
        letter = "D"
    elif 0.0 <= score < 3.0:
        letter = "F"
    return letter

print("Score 9.5:", score(9.5))
print("Score 7.0:", score(7.0))
print("Score 5.5:", score(5.5))
print("Score 3.2:", score(3.2))
print("Score 1.0:", score(1.0))