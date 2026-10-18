# Online Python compiler (interpreter)
# Write and run Python online using this editor.



import pandas as pd
import numpy as np
from io import StringIO

# Step 1: Create the student dataset
csv_data = """Student_ID,Name,Department,Python,Maths,AI,Attendance
1,Rahul,IT,85,78,92,95
2,Priya,CSE,91,88,89,98
3,Sam,IT,65,58,70,80
4,Karan,CSE,45,81,62,75
5,Venny,ECE,78,72,64,88
6,Aditi,AIDS,76,87,64,54
7,Ali,CSE,75,89,75,89
8,Brian,IT,74,84,89,95
9,Aman,EEE,78,85,87,94
10,Sarah,AIDS,89,86,88,79
11,Zarah,IT,85,88,86,75
12,Zoya,ECE,94,97,89,88
13,Ibrahim,CSE,75,85,87,89
14,Alyana,CSE,68,74,84,75
15,Paul,AIDS,88,76,85,86"""

# Step 2: Load the dataset into Pandas
df = pd.read_csv(StringIO(csv_data))

print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
print("\nOriginal Student Data:")
print(df.to_string(index=False))

# Step 3: Calculate total and average marks
subjects = ["Python", "Maths", "AI"]

df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1).round(2)

print("\nSTUDENT MARKS SUMMARY")
print(df[["Name", "Total", "Average"]].to_string(index=False))

# Step 4: Assign grades to students
def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


# Step 5: Check pass or fail
def check_result(row):
    if all(row[subject] >= 40 for subject in subjects):
        return "Pass"
    else:
        return "Fail"


# Apply the functions to the dataset
df["Grade"] = df["Average"].apply(calculate_grade)
df["Result"] = df.apply(check_result, axis=1)

# Display the updated results
print("\nSTUDENT GRADES AND RESULTS")
print(
    df[["Name", "Average", "Grade", "Result"]]
    .to_string(index=False)
)

# Step 6: Overall class performance analysis

print("\nCLASS PERFORMANCE ANALYSIS")

# Calculate class average
class_average = np.mean(df["Average"])
print("Overall Class Average:", round(class_average, 2))

# Find the highest average
highest_average = df["Average"].max()
print("Highest Student Average:", highest_average)

# Display the top-performing student(s)
print("\nTOP PERFORMING STUDENT(S):")
print(
    df.loc[df["Average"] == highest_average,
           ["Name", "Department", "Average", "Grade"]]
    .to_string(index=False)
)

# Find the lowest average
lowest_average = df["Average"].min()
print("Lowest Student Average:", lowest_average)

# Count pass and fail students
passed = (df["Result"] == "Pass").sum()
failed = (df["Result"] == "Fail").sum()

print("Students Passed:", passed)
print("Students Failed:", failed)
print("Total Students:", len(df))

# Step 7: Subject-wise performance analysis

print("\nSUBJECT-WISE PERFORMANCE ANALYSIS")

# Calculate average marks for each subject
subject_averages = df[subjects].mean()

for subject, average in subject_averages.items():
    print(f"{subject} Average: {average:.2f}")

# Find the subject with the highest average
best_subject = subject_averages.idxmax()
best_average = subject_averages.max()

print("\nBest Performing Subject:", best_subject)
print("Subject Average:", round(best_average, 2))

# Find the subject with the lowest average
lowest_subject = subject_averages.idxmin()
lowest_subject_average = subject_averages.min()

print("Lowest Performing Subject:", lowest_subject)
print("Subject Average:", round(lowest_subject_average, 2))

# Step 8: Top 3 performing students

print("\nTOP 3 PERFORMING STUDENTS")

top_students = df.sort_values(
    by="Average",
    ascending=False
).head(3)

print(
    top_students[
        ["Student_ID", "Name", "Department", "Average", "Grade"]
    ].to_string(index=False)
)
