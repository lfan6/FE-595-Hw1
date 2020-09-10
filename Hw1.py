# Lucas Fan
# FE-595 Python Refresher
# Create and Display the graph of one period (0 to 2pi) of the sine and cosine functions

# Importing Pacakges
import numpy as np
import matplotlib.pyplot as plt

# Creating Period (x axis)
per = np.arange(0, 2*np.pi, 0.1)

# Creating Sine and Cosine functions (y axis)
sin = np.sin(per)
cos = np.cos(per)
tan = np.tan(per)

# Creating graph, with title and labels
plt.plot(per, sin, per, cos, per, tan)
plt.title("Sine, Cosine, and Tangent")
plt.legend(['Sine Function', 'Cosine Function', 'Tangent Function'])
plt.ylim(-4,4)
plt.show()

# TODO: I would suggest adding a main and putting this code into a function that gets called from the main.
