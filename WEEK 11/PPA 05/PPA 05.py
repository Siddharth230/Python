import numpy as np
import matplotlib.pyplot as plt

# Define the radius of the circle
r = 5

# Generate a set of angles from 0 to 2*pi
# A larger number of points will make the circle smoother
theta = np.linspace(0, 2 * np.pi, 500)

# Calculate the x and y coordinates using the parametric equations of a circle
# x = r * cos(theta)
# y = r * sin(theta)
x = r * np.cos(theta)
y = r * np.sin(theta)

# Create the figure and axes for the plot
fig, ax = plt.subplots(figsize=(7, 7))

# Create the scatter plot
ax.scatter(x, y, s=5)  # s is the marker size

# --- Important: Set the aspect ratio to 'equal' ---
# This ensures that the circle is not distorted into an ellipse
# It makes one unit on the x-axis equal to one unit on the y-axis
ax.set_aspect("equal", adjustable="box")

# Add a title and labels
ax.set_title(f"Scatter Plot of a Circle with Radius r={r}")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

# Add a grid for better visualization
ax.grid(True, linestyle="--")

# Set the limits for the x and y axes to be slightly larger than the radius
ax.set_xlim(-r - 1, r + 1)
ax.set_ylim(-r - 1, r + 1)

# Save the plot to a file
plt.savefig("circle_scatter_plot.png")
