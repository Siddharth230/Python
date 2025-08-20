import numpy as np
import matplotlib.pyplot as plt

# The number of trials for each experiment
n_values = [10, 100, 1000, 10000, 100000, 1000000]

# The possible outcomes of a single dice roll
outcomes = np.arange(1, 7)

# The theoretical probability for an unbiased six-sided die
theoretical_prob = 1 / 6

# Create a figure with 3 rows and 2 columns of subplots
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(12, 14))
# Flatten the 2D array of axes to a 1D array for easy iteration
axes = axes.flatten()

# Loop through each value of n and its corresponding subplot axis
for n, ax in zip(n_values, axes):
    # (1) Throw a standard, unbiased, six-sided dice n times.
    rolls = np.random.randint(1, 7, size=n)

    # (2) Get the frequency of occurrence of the numbers from 1 to 6.
    # We ensure all outcomes (1-6) are represented, even if they don't appear in the rolls.
    frequencies = np.zeros(6, dtype=int)
    unique_outcomes, counts = np.unique(rolls, return_counts=True)
    frequencies[unique_outcomes - 1] = counts  # -1 to match 0-based index

    # (3) Convert the frequencies to probabilities.
    probabilities = frequencies / n

    # (4) Represent the probabilities in the form of a bar plot.
    ax.bar(outcomes, probabilities, label="Experimental")

    # Add a line for the theoretical probability for comparison
    ax.axhline(y=theoretical_prob, color="r", linestyle="--", label="Theoretical (1/6)")

    # Set titles and labels for each subplot
    ax.set_title(f"n = {n:,}")  # Use comma for thousands separator
    ax.set_xlabel("Die Face")
    ax.set_ylabel("Probability")
    ax.set_ylim(0, 0.5)  # Use a fixed y-axis for fair comparison
    ax.legend()

# Add a main title for the entire figure and adjust layout
plt.suptitle("Probability Distribution of a Six-Sided Die Roll", fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Save the final figure
plt.savefig("dice_roll_experiment.png")

plt.close()

print("Experiment complete. Plot saved as 'dice_roll_experiment.png'")
