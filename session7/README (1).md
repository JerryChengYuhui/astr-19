# JerryCheng Session 7, Code Journal 2

This Python script shows how to use the matplotlib plot exp(x).

## Function Overview

- `import numpy as np`: imports the numpy library

- `import matplotlib.pyplot as plt`: imports the pyplot module from matplotlib

- `np.linspace(0, 1, 100)`: Creates an array `x` that starts at 0, ends at 1, and contains 100points

- `def exp_function(x): return np.exp(x)`: Defines a function named `exp_function` that takes an argument `x` and returns `exp(x)`

- `plt.plot(x, y)`: Generates the plot using `x` and `y`

- `plt.xlabel('Time [milliseconds]')`: Sets the label for the x-axis to [milliseconds]

- `plt.ylabel('Awesomeness')`: Sets the label for the y-axis to Awesomeness

- `plt.title('Plot of exp(x)')`: Sets the title of the plot to Plot of exp(x)


