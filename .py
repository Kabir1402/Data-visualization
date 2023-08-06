import pandas as pd

# Load the cleaned merged CSV file
cleaned_merged_df = pd.read_csv('cleaned_merged_stars.csv')

# Convert mass into kilograms by multiplying with 1.989e+30
cleaned_merged_df['Mass'] *= 1.989e+30

# Convert radius into meters by multiplying with 6.957e+8
cleaned_merged_df['Radius'] *= 6.957e+8

# Make an empty list to store gravity values
gravity_values = []

# Write a function to calculate gravity
def calculate_gravity(mass, radius):
    G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
    gravity = (G * mass) / (radius ** 2)
    return gravity

# Calculate gravity for each row and append to gravity_values list
for index, row in cleaned_merged_df.iterrows():
    gravity = calculate_gravity(row['Mass'], row['Radius'])
    gravity_values.append(gravity)

# Add the gravity column to the DataFrame
cleaned_merged_df['Gravity'] = gravity_values

# Save the updated DataFrame to a new CSV file
final_dataset_csv = 'final_dataset.csv'
cleaned_merged_df.to_csv(final_dataset_csv, index=False)

print("Final dataset saved to 'final_dataset.csv'")

import matplotlib.pyplot as plt

final_df = pd.read_csv(final_dataset_csv)

# Create lists of mass, radius, and gravity data
mass_data = final_df['Mass'].tolist()
radius_data = final_df['Radius'].tolist()
gravity_data = final_df['Gravity'].tolist()

# Sort the lists
mass_data.sort()
radius_data.sort()
gravity_data.sort()

# Create a chart of mass vs. radius using Matplotlib
plt.figure(figsize=(10, 6))
plt.scatter(mass_data, radius_data, color='blue', marker='o')
plt.xlabel('Mass (kg)')
plt.ylabel('Radius (m)')
plt.title('Mass vs. Radius of Stars')
plt.grid(True)
plt.show()

# Create a chart of mass vs. gravity using Matplotlib
plt.figure(figsize=(10, 6))
plt.scatter(mass_data, gravity_data, color='red', marker='x')
plt.xlabel('Mass (kg)')
plt.ylabel('Gravity (m/s^2)')
plt.title('Mass vs. Gravity of Stars')
plt.grid(True)
plt.show()
  