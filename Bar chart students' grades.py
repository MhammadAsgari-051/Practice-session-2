
import matplotlib.pyplot as plt

students = ["Ali", "Reza", "Sara", "Maryam", "Amir"]

grades = [18, 15, 19, 16, 12]

plt.figure(figsize=(9, 5))

plt.bar(students, grades)

plt.xlabel("Students")
plt.ylabel("Grade")
plt.title("Student Grades Comparison")

plt.ylim(0, 20)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.show()
