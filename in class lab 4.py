###############
# Darcy Warms #
# HSC 4933    #
# IC 4        #
###############

# Imports

import pandas as pd
import numpy as np

df = pd.read_csv("eyes.csv")
print(df.shape,
      df.dtypes,
      df.isna().sum(), # Print total number of NaN values
      df.nunique(),
      sep="\n")


print("Duplicates: ", df.duplicated().sum()) # Print number of duplicated values

df = df.dropna(axis=1, how="all") # Drop columns with no data (only NaN)
df = df.drop(columns = [c for c in df.columns if c.endswith("ID")]) # Drop columns that end in ID

df = df.dropna(subset=["Data_Value"]) # Drop rows with no value in the column "Data_Value"
df = df.drop(columns=["Geolocation", "Data_Value_Footnote_Symbol", "Data_Value_Footnote", \
                        "StateAbbr", "NonWeightedSample", "Geographic Level", "Numerator"])

df.columns = df.columns.str.lower().str.replace(" ", "_") # Makes column headers snake_case

# Create new column "error"
df["error"] = (df["high_confidence_limit"] - df["low_confidence_limit"]) / 2
df["prevalence_level"] = np.select([df["data_value"] < 5, df["data_value"] <= 7], \
                                   ["Low", "Medium"], "High") # Create prevalence level description column

# Save to csv
df.to_csv("eye_health_2022_clean.csv", index=False)

# Print dimensions (number of rows and columns) to verify save
print(pd.read_csv("eye_health_2022_clean.csv").shape == df.shape) # Print t/f if dimensions match
print(pd.read_csv("eye_health_2022_clean.csv").shape) # Print saved file dimensions
print(pd.read_csv("eye_health_2022_clean.csv").head) # Print dataframe head (first 5 lines)