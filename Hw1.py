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

# Creating graph, with title and labels
plt.plot(per, sin, per, cos)
plt.title("Sine and Cosine")
plt.legend(['Sine Function', 'Cosine Function'])
plt.show()
