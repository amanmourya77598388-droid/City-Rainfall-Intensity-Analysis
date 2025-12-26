import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ===============================
# Step 1: Create Rainfall Dataset
# ===============================
np.random.seed(42)

dates = pd.date_range(start="2024-01-01", periods=120)
rainfall = np.random.gamma(shape=2, scale=6, size=120)

# Extreme rainfall events
rainfall[20] = 65
rainfall[70] = 90
rainfall[105] = 75

df = pd.DataFrame({
    "Date": dates,
    "Rainfall_mm": rainfall
})

print("Sample Data:")
print(df.head())

# ===============================
# Step 2: Z-Score Calculation
# ===============================
mean = df["Rainfall_mm"].mean()
std = df["Rainfall_mm"].std()

df["Z_score"] = (df["Rainfall_mm"] - mean) / std
df["Extreme_Event"] = df["Z_score"].abs() > 2

print("\nExtreme Rainfall Events:")
print(df[df["Extreme_Event"]])

# ===============================
# Step 3: Plot Graph
# ===============================
plt.figure(figsize=(12,5))
plt.plot(df["Date"], df["Rainfall_mm"], label="Rainfall Intensity")
plt.scatter(
    df[df["Extreme_Event"]]["Date"],
    df[df["Extreme_Event"]]["Rainfall_mm"],
    label="Extreme Event"
)

plt.xlabel("Date")
plt.ylabel("Rainfall (mm)")
plt.title("City Rainfall Intensity Analysis")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()