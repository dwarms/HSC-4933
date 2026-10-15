#############################
# Darcy Warms               #
# Lab 7 : Linear Regression #
# HSC 4933                  #
# 10/8/26                   #
#############################

# Imports

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm

# Prompt user for dataset

print("Available datasets: ")
print("1. birthwt.csv")
print("2. places_2025.csv")

dataset_choice = input("Please enter your dataset : ")

if dataset_choice == "1":
    CSV_path = "birthwt.csv"

elif dataset_choice == "1. birthwt.csv":
    CSV_path = "birthwt.csv"

elif dataset_choice == "birthwt.csv":
    CSV_path = "birthwt.csv"

elif dataset_choice == "2":
    CSV_path = "places_2025.csv"

elif dataset_choice == "2. places_2025.csv":
    CSV_path = "places_2025.csv"

elif dataset_choice == "places_2025.csv":
    CSV_path = "places_2025.csv"

else:
    print("Invalid choice. Please try again.")

# Load .csv

df = pd.read_csv(CSV_path, thousands=",")

# Convert headings to snake case

df.columns = df.columns.str.lower().str.replace(" ", "_")

# List available column names

print("Available columns: ")
print(df.columns.tolist())

# Prompt user to name X and Y variables

X_COL = input("Please name your X variable: ")
Y_COL = input("Please name your Y variable: ")

# Drop rows with missing values

data = df[[X_COL, Y_COL]].dropna()

# Create scatterplot

fig,ax = plt.subplots(figsize=(8, 6))
ax.scatter(data[X_COL], data[Y_COL], alpha=0.6, edgecolor="k", linewidth=0.3)
ax.set_xlabel(X_COL)
ax.set_ylabel(Y_COL)
ax.set_title(f"{Y_COL} vs {X_COL} (n = {len(data)})")
ax.grid(alpha=0.3)
fig.tight_layout()

# Ask user if they want to save file

save_scatter = input("Would you like to save this scatterplot? (y/n): ")
if save_scatter == "y":
    scatter_file = input("Please enter a file name: ")
    plt.savefig(scatter_file, dpi=300)
    print(f"Saved scatterplot to {scatter_file}")

# Perform linear regression

X = sm.add_constant(data[X_COL])
model = sm.OLS(data[Y_COL], X).fit()

# Print summary

print("OLS Regression Summary: ")
print(model.summary())
# Print values needed for trends document
print("Intercept (β0):", model.params["const"])
print("Slope (β1):", model.params[X_COL])
print("R²:", model.rsquared)

# Create new scatterplot with regression

x_line = np.linspace(data[X_COL].min(), data[X_COL].max(), 100)
y_line = model.params["const"] + model.params[X_COL] * x_line
ax.plot(x_line, y_line, color="crimson", linewidth=2, label=f"OLS line (R² = {model.rsquared:.3f})")
ax.set_title(f"{Y_COL} vs {X_COL} with OLS line (n = {len(data)})")
ax.legend()

# Ask user if they want to save scatterplot with regression line

save_scatter = input("Would you like to save this scatterplot with OLS regression line? (y/n): ")
if save_scatter == "y":
    scatter_file = input("Please enter a file name: ")
    plt.savefig(scatter_file, dpi=300)
    print(f"Saved scatterplot to {scatter_file}")

# Display scatterplot

plt.show()

