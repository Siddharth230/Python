import numpy as np
import matplotlib.pyplot as plt

# Create a range of x values from -2*pi to 2*pi
x = np.linspace(-2 * np.pi, 2 * np.pi, 400)

# Calculate the y values for sin(x) and cos(x)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Create the plot
plt.figure(figsize=(8, 6))  # Set a nice figure size

# Plot sin(x) with a label for the legend
plt.plot(x, y_sin, label=r"$\sin(x)$")

# Plot cos(x) with a label for the legend
plt.plot(x, y_cos, label=r"$\cos(x)$")

# Add a title to the graph
plt.title(r"Plot of $\sin(x)$ and $\cos(x)$")

# Add labels for the x and y axes
plt.xlabel("x (radians)")
plt.ylabel("Function Value")

# Add a legend to distinguish the lines
plt.legend()

# Add a grid for better readability
plt.grid(True)

# Save the plot to a file
plt.savefig("sin_cos_plot.png")
