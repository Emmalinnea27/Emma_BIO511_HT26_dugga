# Question 3 - C
# Now we want to allow for user input to change the input and output files. Testing avoidance of hardcoding while reading in files.
# We will do this using argparse, import it and integrate into code! Choosing to write a new code below rather than integrate into the above, for clarity.

import argparse
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

input_file = input("Enter the input filename: ")
output_file = input("Enter the output plot filename: ")


plot_title = input("Enter the plot title: ")
x_label = input("Enter the x-axis title: ")
y_label = input("Enter the y-axis title: ")


df = pd.read_csv(input_file, sep=r'\s+')

sns.scatterplot(
    data=df,
    x="position_mb",
    y="log2_ratio"
)

plt.title(plot_title)
plt.xlabel(x_label)
plt.ylabel(y_label)

plt.savefig(output_file)
plt.show()