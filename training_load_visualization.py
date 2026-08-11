# ==========================================
# Athlete Training Load Visualization
# Day 9 - Sports Data Analytics
# Author: Abhishek Tomar
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt


print("=" * 70)
print("          ATHLETE TRAINING LOAD VISUALIZATION")
print("=" * 70)


# ------------------------------------------
# Load Dataset
# ------------------------------------------

data = pd.read_csv("training_data.csv")

data["Date"] = pd.to_datetime(data["Date"])


# ------------------------------------------
# Calculate Training Load
# ------------------------------------------

data["Training_Load"] = (
    data["Duration_min"] * data["sRPE"]
)


# ------------------------------------------
# Display Basic Information
# ------------------------------------------

print("\nDATASET INFORMATION")
print("=" * 70)

print(f"Number of Sessions : {len(data)}")
print(f"Number of Athletes : {data['Athlete'].nunique()}")
print(f"Total Training Load: {data['Training_Load'].sum():.0f} AU")


# ------------------------------------------
# Athlete Training Load
# ------------------------------------------

athlete_load = (
    data.groupby("Athlete")["Training_Load"]
    .sum()
    .sort_values(ascending=False)
)


print("\nATHLETE TOTAL TRAINING LOAD")
print("=" * 70)

for athlete, load in athlete_load.items():
    print(f"{athlete:<10} : {load:.0f} AU")


# ------------------------------------------
# Daily Team Training Load
# ------------------------------------------

daily_load = (
    data.groupby("Date")["Training_Load"]
    .sum()
)


print("\nDAILY TEAM TRAINING LOAD")
print("=" * 70)

for date, load in daily_load.items():
    print(f"{date.date()} : {load:.0f} AU")


# ------------------------------------------
# Visualization 1
# Athlete Total Load
# ------------------------------------------

plt.figure()

athlete_load.plot(kind="bar")

plt.title("Total Training Load by Athlete")
plt.xlabel("Athlete")
plt.ylabel("Training Load (AU)")

plt.tight_layout()

plt.savefig("athlete_total_training_load.png")

plt.show()


# ------------------------------------------
# Visualization 2
# Daily Training Load
# ------------------------------------------

plt.figure()

daily_load.plot(kind="line", marker="o")

plt.title("Daily Team Training Load")
plt.xlabel("Date")
plt.ylabel("Training Load (AU)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("daily_training_load.png")

plt.show()


# ------------------------------------------
# Visualization 3
# Session Type Load
# ------------------------------------------

session_type_load = (
    data.groupby("Session_Type")["Training_Load"]
    .sum()
    .sort_values(ascending=False)
)


plt.figure()

session_type_load.plot(kind="bar")

plt.title("Training Load by Session Type")
plt.xlabel("Session Type")
plt.ylabel("Training Load (AU)")

plt.tight_layout()

plt.savefig("session_type_training_load.png")

plt.show()


# ------------------------------------------
# Final Message
# ------------------------------------------

print("\n" + "=" * 70)
print("VISUALIZATION COMPLETE")
print("=" * 70)

print("\nCharts created:")
print("1. athlete_total_training_load.png")
print("2. daily_training_load.png")
print("3. session_type_training_load.png")

print("\n" + "=" * 70)
print("Train Smart • Analyze Data • Improve Performance")
print("=" * 70)