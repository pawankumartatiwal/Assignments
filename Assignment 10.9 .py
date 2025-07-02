import matplotlib.pyplot as plt

semesters = ['Sem 1', 'Sem 2']
gpa = [8.2, 8.7]
plt.figure(figsize=(6, 4))
plt.plot(semesters, gpa, marker='o', linestyle='-', color='blue', label='GPA Trend')
plt.title('Semester GPA Comparison')
plt.xlabel('Semester')
plt.ylabel('GPA')
plt.ylim(0, 10)
plt.grid(True)
plt.legend()
plt.show()
