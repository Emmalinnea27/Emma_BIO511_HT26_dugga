# Question 3 - C
# Now we want to allow for user input to change the input and output files. Testing avoidance of hardcoding while reading in files.
# We will do this using argparse, import it and integrate into code! Choosing to write a new code below rather than integrate into the above, for clarity.

import argparse
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--input", help = "Input CSV file")
parser.add_argument("--output", help = "Output plot filename")
args = parser.parse_args()

df = pd.read_csv(args.input, sep=r'\s+')

sns.scatterplot(
    data=df,
    x="position_mb",
    y="log2_ratio",
)
plt.savefig(args.output)
plt.show()