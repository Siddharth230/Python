import pandas as pd
import matplotlib.pyplot as plt

# The data for the CSV file
csv_data = """Maths,Physics
20,80
10,30
40,30
20,30
10,5
80,90
99,100
76,84
29,100
100,30
95,92
100,100
70,74
65,88
90,93
89,91
20,40
10,30
20,25
15,34
35,25
50,70
45,55
34,43
60,67
"""

# Create the scores.csv file
with open("scores.csv", "w") as f:
    f.write(csv_data)

# Read the data from the CSV file using pandas
df = pd.read_csv("scores.csv")

# Extract the scores for each subject
math_scores = df["Maths"]
physics_scores = df["Physics"]

# Create the scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(math_scores, physics_scores)

# Add a title and axis labels for clarity
plt.title("Scatter Plot of Mathematics vs. Physics Scores")
plt.xlabel("Mathematics Scores")
plt.ylabel("Physics Scores")
plt.grid(True)

# Save the plot as an image file
plt.savefig("scores_scatter_plot.png")
