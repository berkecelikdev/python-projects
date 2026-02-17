import numpy as np
import matplotlib.pyplot as plt

# 50 students, 2 exams (Column 0: Midterm, Column 1: Final)
grades = np.random.randint(0, 101, size=(50, 2))

print(f"Dataset Shape: {grades.shape}")
print("Grades of the First 5 Students:\n", grades[:5])
print("-" * 30)

# 2. CALCULATING AVERAGES (Vectorization)
# Processing all columns without using loops
# Multiplying Column 0 by 40%, Column 1 by 60%
year_end_grades = (grades[:, 0] * 0.4) + (grades[:, 1] * 0.6)

print("Year-End Averages of the First 5 Students: ", year_end_grades[:5])
print("-" * 30)

# 3. STATISTICS
class_average = np.mean(year_end_grades)
highest_grade = np.max(year_end_grades)
top_student_index = np.argmax(year_end_grades)
std_deviation = np.std(year_end_grades)

print(f"Class Average: {class_average:.2f}")
print(f"Highest Grade: {highest_grade} (Student Index: {top_student_index})")
print(f"Standard Deviation: {std_deviation:.2f}")
print("-" * 30)

# 4. FILTERING (Boolean Indexing)
# Those with grades lower than 50 (Returns a True/False array)
failed_mask = year_end_grades < 50

# We extract the grades using this mask
failing_student_grades = year_end_grades[failed_mask]

print(f"Number of Students Failed: {len(failing_student_grades)}")
# The '~' sign takes the inverse (NOT), meaning those who passed.
print(f"Average of Those Who Passed: {np.mean(year_end_grades[~failed_mask]):.2f}")

# 1. Creating Histogram
# bins=10: Divides grades into 10-point intervals (0-10, 10-20, etc.)
# alpha=0.7: Transparency of the bars (for visuals)
# color='skyblue': Bar color
# edgecolor='black': Border line of the bars (to make them look clearer)
plt.figure(figsize=(10, 6)) # Adjusting the size of the graph
plt.hist(year_end_grades, bins=10, range=(0, 100), color='skyblue', edgecolor='black', alpha=0.7)

# 2. Adding Average Line (Vertical Line)
# axvline: Axis Vertical Line
plt.axvline(np.mean(year_end_grades), color='red', linestyle='dashed', linewidth=2, label=f"Average: {np.mean(year_end_grades):.2f}")

# 3. Titles and Labels
plt.title("Class Year-End Grade Distribution", fontsize=15)
plt.xlabel("Grades (0-100 Range)", fontsize=12)
plt.ylabel("Number of Students", fontsize=12)
plt.legend() # Necessary to show the "Average" label
plt.grid(axis="y", alpha=0.5) # Only horizontal lines
plt.show()
