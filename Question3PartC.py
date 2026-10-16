# Question 3 - C
# Now we want to allow for user input to change the input and output files. Testing avoidance of hardcoding while reading in files.
# Allows us to read in information as user input rather than hardcoding

import argparse
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Allows user to input 
input_file = input("Enter the input filename: ")
output_file = input("Enter the output plot filename: ")

# Allows user to input the title and axis info
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