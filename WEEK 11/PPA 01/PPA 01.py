import numpy as np
import matplotlib.pyplot as plt

# Function 1: f(x) = 3x - 4
x1 = np.linspace(-10, 10, 400)
y1 = 3 * x1 - 4

plt.plot(x1, y1)
plt.title("$f(x) = 3x - 4$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.savefig("plot1.png")
plt.clf()

# Function 2: f(x) = x^2 + 2x - 15
x2 = np.linspace(-10, 10, 400)
y2 = x2**2 + 2 * x2 - 15

plt.plot(x2, y2)
plt.title("$f(x) = x^2 + 2x - 15$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.savefig("plot2.png")
plt.clf()

# Function 3: f(x) = 5(x-1)(x-2)(x-3)
x3 = np.linspace(-1, 5, 400)
y3 = 5 * (x3 - 1) * (x3 - 2) * (x3 - 3)

plt.plot(x3, y3)
plt.title("$f(x) = 5(x-1)(x-2)(x-3)$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.savefig("plot3.png")
plt.clf()

# Function 4: f(x) = e^x
x4 = np.linspace(-5, 5, 400)
y4 = np.exp(x4)

plt.plot(x4, y4)
plt.title("$f(x) = e^x$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.savefig("plot4.png")
plt.clf()

# Function 5: f(x) = log(x)
# Note: log(x) is defined for x > 0
x5 = np.linspace(0.1, 10, 400)
y5 = np.log(x5)

plt.plot(x5, y5)
plt.title(r"$f(x) = \log(x)$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.savefig("plot5.png")
plt.clf()

# Function 6: f(x) = sin(x)
x6 = np.linspace(-2 * np.pi, 2 * np.pi, 400)
y6 = np.sin(x6)

plt.plot(x6, y6)
plt.title(r"$f(x) = \sin(x)$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.savefig("plot6.png")
plt.clf()

print("All plots saved successfully.")
