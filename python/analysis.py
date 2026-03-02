import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../sample_data/students.csv")

print("\n--- Student Performance Report ---")

# Basic statistics
print("Average Score:", df["Score"].mean())
print("Highest Score:", df["Score"].max())
print("Lowest Score:", df["Score"].min())

# Top student
top_student = df.loc[df["Score"].idxmax()]
print("\nTop Performer:")
print(top_student)

# Chart
df.groupby("Subject")["Score"].mean().plot(kind="bar")
plt.title("Average Score per Subject")
plt.xlabel("Subject")
plt.ylabel("Average Score")
plt.savefig("performance_report.png")

print("\nReport generated: performance_report.png")
