students = [
    {"name": "Ana", "grades": [8.5, 7.0, 9.0]},
    {"name": "Luis", "grades": [5.0, 4.5, 6.0]},
    {"name": "Maria", "grades": [9.5, 9.0, 10.0]},
    {"name": "Pedro", "grades": [3.0, 4.0, 2.5]},
    {"name": "Sofia", "grades": [7.0, 7.5, 8.0]},
]


def average(grades):
    total = 0
    for grade in grades:
        total += grade
    return total / len(grades)


def get_status(avg):
    if avg >= 5.0:
        mark = "PASS"
    else:
        mark = "FAIL"
    return mark

def main():
    passed_count = 0
    failed_count = 0

    for student in students:
        name = student["name"]
        avg = average(student["grades"])
        status = get_status(avg)

        print(f"{name}: {avg:.1f} -> {status}")

        if status == "PASS":
            passed_count += 1
        else:
            failed_count += 1

    print(f"\nResults: {passed_count} passed, {failed_count} failed")


main()