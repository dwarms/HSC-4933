###########################
# Darcy Warms             #
# Lab 5 : Data Conversion #
# HSC 4933                #
###########################

# Import pandas

import pandas as pd

# Load .csv file

df = pd.read_csv("maternalhealth.csv")

# Find and remove duplicates

print("Are there duplicated columns?: ", df.columns.duplicated().any())

# Save the .csv as .xlsx

df.to_excel("maternalhealth.xlsx", index=False)
