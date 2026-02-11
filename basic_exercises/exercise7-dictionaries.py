student = {
    "name": "Carlos",
    "age": 22,
    "subjects": ["PNE", "Networks", "Databases"],
    "grades": {"PNE": 8.5, "Networks": 7.0, "Databases": 9.2}
}

count = 0
for i in student["grades"].values():
    count += i
    avg = round(count / len(student["grades"]), 2)

def subject_grade_pairs(student):
    grades = student["grades"]
    for subject, grade in grades.items():
        print(f"{subject}: {grade}")


def main():
    print("Name:", student["name"])
    print("Number of subjets:", len(student["subjects"]))
    print("Enrolled in PNE:", "PNE" in student["subjects"])
    print("Databases grade:", student["grades"]["Databases"])
    print("Average grade: ", avg)
    print("Subject grades:")
    subject_grade_pairs(student)

main()
