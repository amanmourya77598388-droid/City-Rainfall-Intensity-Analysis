# City-Rainfall-Intensity-Analysis
## 🔹 Project Objective

The objective of this project is to:

* Analyze daily rainfall data of a city
* Identify **extreme rainfall events**
* Use the **Z-Score method** to detect unusual rainfall values
* Visualize rainfall trends using graphs

---

## 🔹 Step 1: Import Required Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

### Explanation:

* **Pandas** is used to store and manage data in tabular form
* **NumPy** is used for numerical calculations and random data generation
* **Matplotlib** is used for plotting graphs

---

## 🔹 Step 2: Create Rainfall Dataset

```python
np.random.seed(42)
```

This ensures the same random rainfall values are generated every time.

```python
dates = pd.date_range(start="2024-01-01", periods=120)
```

This creates 120 consecutive dates starting from January 1, 2024.

```python
rainfall = np.random.gamma(shape=2, scale=6, size=120)
```

Gamma distribution is used to generate realistic rainfall data.

---

## 🔹 Step 3: Add Extreme Rainfall Events

```python
rainfall[20] = 65
rainfall[70] = 90
rainfall[105] = 75
```

These values represent **extreme rainfall events**, such as heavy rain or flooding days.

---

## 🔹 Step 4: Create DataFrame

```python
df = pd.DataFrame({
    "Date": dates,
    "Rainfall_mm": rainfall
})
```

The data is stored in a DataFrame with:

* Date
* Rainfall in millimeters

```python
print(df.head())
```

This displays the first five rows of the dataset.

---

## 🔹 Step 5: Z-Score Calculation

```python
mean = df["Rainfall_mm"].mean()
std = df["Rainfall_mm"].std()
```

The **mean (average)** and **standard deviation** of rainfall are calculated.

```python
df["Z_score"] = (df["Rainfall_mm"] - mean) / std
```

Z-Score formula used:

[
Z = \frac{(Value - Mean)}{Standard\ Deviation}
]

---

## 🔹 Step 6: Identify Extreme Rainfall Events

```python
df["Extreme_Event"] = df["Z_score"].abs() > 2
```

Rule used:

* If |Z-Score| > 2 → the rainfall value is considered **extreme**

```python
print(df[df["Extreme_Event"]])
```

This prints only the extreme rainfall days.

---

## 🔹 Step 7: Plot Rainfall Graph

```python
plt.figure(figsize=(12,5))
plt.plot(df["Date"], df["Rainfall_mm"], label="Rainfall Intensity")
```

A line graph shows daily rainfall trends.

```python
plt.scatter(
    df[df["Extreme_Event"]]["Date"],
    df[df["Extreme_Event"]]["Rainfall_mm"],
    label="Extreme Event"
)
```

Scatter points highlight extreme rainfall events.

```python
plt.xlabel("Date")
plt.ylabel("Rainfall (mm)")
plt.title("City Rainfall Intensity Analysis")
plt.legend()
plt.show()
```

---

## 🔹 Project Conclusion

* Rainfall intensity varies over time
* Z-Score method effectively identifies extreme rainfall events
* Extreme rainfall days stand out clearly in the graph
* This approach is useful for **weather analysis and flood risk assessment**

---

