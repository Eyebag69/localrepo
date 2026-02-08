import numpy as np
import matplotlib.pyplot as plt

marks = np.array([
    [80,75,90,85],
    [60,70,65,72],
    [95,88,92,90],
    [78,82,80,79]
])

total_per_student = marks.sum(axis = 1)
print(total_per_student)

highest_per_student = total_per_student.max(axis = 0)
print(highest_per_student)

avg_per_student = total_per_student.mean(axis = 1)
print(avg_per_student)

top3_indices = avg_per_student.argsort()[::-1][:3]
print(top3_indices)

student = np.arrange(1,6)
plt.bar(student, total_per_student)
plt.xlabel('Student')
plt.ylabel("Total Marks per Student")
plt.title("Total Marks per Student")
plt.show()
