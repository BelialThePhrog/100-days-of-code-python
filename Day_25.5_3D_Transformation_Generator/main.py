import numpy as np
import time
import matplotlib.pyplot as plt

N = 1_000_000
print(f"Generating data: vector of  {N} elements...\n")
#Creating array of 1M data with (x,y,z) coordintaes
generated_data = np.random.rand(N,3)
# add a column
column_of_ones = np.ones(N)
new_data = np.column_stack((generated_data, column_of_ones))
print(new_data)
#Creating rotation matrix
Degrees = float(input("Please specify how much degrees would you like to rotate?"))
theta = np.radians(Degrees)
c, s = np.cos(theta), np.sin(theta)
R_3d = np.array([
    [ c,   s,  0.0, 0.0],
    [-s,   c,  0.0, 0.0],
    [0.0, 0.0, 1.0, 0.0],
    [0.0, 0.0, 0.0, 1.0]
])
print(R) 
# Creating translation matrix
tx = float(input("Please specify the tx value?"))
ty = float(input("Please specify the ty value?"))
tz = float(input("Please specify the tz value?"))
T_3d = np.array([
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 1.0, 0.0],
    [tx,  ty,  tz,  1.0]
])

Combined_Transform = np.matmul(T_3d, R_3d)
start_time = time.perf_counter()
final_data = np.matmul(new_data, Combined_Transform)
time_to_complete = time.perf_counter() - start_time
print(final_data)
print(f"It took {time_to_complete:.5f} seconds")
# VISUALIZATION SECTION
print("Generating 3D plots...")

# Taking only the first 500 points for immediate rendering and clarity
sample_size = 500

# Creating the main figure window
fig = plt.figure(figsize=(12, 6))

# Plot 1: Raw data (Before transformation)
ax1 = fig.add_subplot(121, projection='3d')
ax1.scatter(new_data[:sample_size, 0], new_data[:sample_size, 1], new_data[:sample_size, 2], 
            c='#0275d8', marker='o', alpha=0.6, label='Original')
ax1.set_title('Before Transformation', fontweight='bold')
ax1.set_xlabel('X Axis')
ax1.set_ylabel('Y Axis')
ax1.set_zlabel('Z Axis')
ax1.legend()

# Plot 2: Result (After translation and rotation)
ax2 = fig.add_subplot(122, projection='3d')
ax2.scatter(final_data[:sample_size, 0], final_data[:sample_size, 1], final_data[:sample_size, 2], 
            c='#d9534f', marker='^', alpha=0.6, label='Transformed')
ax2.set_title('After Transformation (Translation + Rotation)', fontweight='bold')
ax2.set_xlabel('X Axis')
ax2.set_ylabel('Y Axis')
ax2.set_zlabel('Z Axis')
ax2.legend()

# Adjusting layout to prevent overlap
plt.tight_layout()
plt.show()
