import matplotlib.pyplot as plt
import numpy as np

# This script will save plots to the 'temp_plots' directory created earlier.
# If it doesn't exist, we create it.
import os
if not os.path.exists('temp_plots'):
    os.makedirs('temp_plots')

# --- Using the Pyplot Interface (State-based) ---
print("--- Pyplot Interface Examples ---")

# 1. Basic Line Plot
print("1. Creating a basic line plot...")
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 6)) # Create a new figure
plt.plot(x, y)
plt.title("Simple Sine Wave")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid(True)
plot_path_1 = 'temp_plots/matplotlib_line_plot.png'
plt.savefig(plot_path_1)
plt.close() # Close the figure to free memory
print(f"   Line plot saved to: {plot_path_1}")


# 2. Scatter Plot
print("2. Creating a scatter plot...")
x_rand = np.random.rand(50)
y_rand = np.random.rand(50)
colors = np.random.rand(50)

plt.figure(figsize=(8, 6))
plt.scatter(x_rand, y_rand, c=colors, s=sizes, alpha=0.5, cmap='viridis')
plt.title("Random Scatter Plot")
plt.xlabel("x value")
plt.ylabel("y value")
plt.colorbar() # Show the color scale
plot_path_2 = 'temp_plots/matplotlib_scatter_plot.png'
plt.savefig(plot_path_2)
plt.close()
print(f"   Scatter plot saved to: {plot_path_2}")


# 3. Bar Chart
print("3. Creating a bar chart...")
categories = ['A', 'B', 'C', 'D']
values = [15, 30, 22, 18]

plt.figure(figsize=(8, 6))
plt.bar(categories, values, color='skyblue')
plt.title("Simple Bar Chart")
plt.xlabel("Category")
plt.ylabel("Value")
plot_path_3 = 'temp_plots/matplotlib_bar_chart.png'
plt.savefig(plot_path_3)
plt.close()
print(f"   Bar chart saved to: {plot_path_3}")


# 4. Histogram
print("4. Creating a histogram...")
data = np.random.randn(1000) # 1000 data points from a standard normal distribution

plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, color='salmon', edgecolor='black')
plt.title("Histogram of a Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plot_path_4 = 'temp_plots/matplotlib_histogram.png'
plt.savefig(plot_path_4)
plt.close()
print(f"   Histogram saved to: {plot_path_4}")


# --- Using the Object-Oriented Interface ---
print("\n--- Object-Oriented Interface Example ---")

# 5. Subplots
print("5. Creating a figure with multiple subplots...")
x = np.linspace(0, 2 * np.pi, 400)
y1 = np.sin(x**2)
y2 = np.cos(x)

# Create a figure and a set of subplots
# fig is the entire figure, ax is an array of Axes objects
fig, axs = plt.subplots(2, 1, figsize=(8, 8)) # 2 rows, 1 column

# Plot on the first axes
axs[0].plot(x, y1, color='purple')
axs[0].set_title('sin(x^2)')
axs[0].set_ylabel('Amplitude')
axs[0].grid(True)

# Plot on the second axes
axs[1].plot(x, y2, color='green')
axs[1].set_title('cos(x)')
axs[1].set_xlabel('x-axis')
axs[1].set_ylabel('Amplitude')
axs[1].grid(True)

# Adjust layout to prevent titles/labels overlapping
fig.tight_layout()

plot_path_5 = 'temp_plots/matplotlib_subplots.png'
plt.savefig(plot_path_5)
plt.close()
print(f"   Subplots figure saved to: {plot_path_5}")


# 6. 3D Plotting
print("6. Creating a 3D surface plot...")
from mpl_toolkits.mplot3d import Axes3D

x_3d = np.arange(-5, 5, 0.25)
y_3d = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(x_3d, y_3d)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(X, Y, Z, cmap='coolwarm')

ax.set_title("3D Surface Plot")
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plot_path_6 = 'temp_plots/matplotlib_3d_plot.png'
plt.savefig(plot_path_6)
plt.close()
print(f"   3D plot saved to: {plot_path_6}")

print("\nAll Matplotlib example plots have been generated and saved.")
