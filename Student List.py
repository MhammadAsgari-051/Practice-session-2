

def sum_grades(courses):
    total = 0

    for grade in courses.values():
        total += grade

    return total



def average(courses):
    return sum_grades(courses) / 8


names = ["Ali", "Reza", "Sara", "Mina", "Amir",
         "Nima", "Maryam", "Hassan", "Zahra", "Arman"]

families = ["Ahmadi", "Mohammadi", "Karimi", "Hosseini",
            "Rezaei", "Moradi", "Jafari", "Rahimi",
            "Kazemi", "Ebrahimi"]

codes = [101, 102, 103, 104, 105, 106, 107, 108]

students = []

for i in range(100):

    student = {}

    student["name"] = names[i % 10]
    student["family"] = families[i // 10]
    student["number"] = 24000001 + i

    courses = {}

    for j in range(8):
        grade = 10 + ((i + j * 3) % 11)
        courses[codes[j]] = grade

    student["courses"] = courses

    students.append(student)


print("-" * 125)

print(f"{'Name':<10} {'Family':<13} {'Number':<12}", end="")

for code in codes:
    print(f"{code:<7}", end="")

print(f"{'Sum':<8} {'Average':<8}")

print("-" * 125)

for student in students:

    courses = student["courses"]

    print(f"{student['name']:<10} {student['family']:<13} "
          f"{student['number']:<12}", end="")

    for code in codes:
        print(f"{courses[code]:<7}", end="")

    print(f"{sum_grades(courses):<8} "
          f"{average(courses):<8.2f}")

print("-" * 125)
