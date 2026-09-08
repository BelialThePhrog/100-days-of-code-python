import matplotlib.pyplot as plt
import numpy as np

# Data Preparation
x = np.linspace(0, 5, 11)
y = x ** 3
z = x ** 2

# --- Exercise 1: Basic OO Plotting ---
print("Rendering Exercise 1...")
fig1 = plt.figure()
ax1 = fig1.add_axes([0, 0, 1, 1])
ax1.plot(x, y, "r-")
ax1.set_xlabel("X label")
ax1.set_ylabel("Y label")
ax1.set_title("Basic OO Plot")
plt.show()

# --- Exercise 2: Multiple Axes on One Figure ---
print("Rendering Exercise 2...")
fig2 = plt.figure()
ax2_main = fig2.add_axes([0, 0, 1, 1])
ax2_inset = fig2.add_axes([0.2, 0.5, 0.2, 0.2])

ax2_main.plot(x, y)
ax2_inset.plot(x, y)
ax2_main.set_title("Main Plot")
ax2_inset.set_title("Inset Plot")
plt.show()

# --- Exercise 3: Customizing Axes Sizes ---
print("Rendering Exercise 3...")
fig3 = plt.figure()
ax3_main = fig3.add_axes([0, 0, 1, 1])
ax3_inset = fig3.add_axes([0.2, 0.5, 0.4, 0.4])

ax3_main.plot(x, y)
ax3_inset.plot(x, z)
plt.show()

# --- Exercise 4: Subplots and Figsize ---
print("Rendering Exercise 4 (Saving to file)...")
fig4, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 2))
plt.tight_layout()

axes[0].plot(x, y, color="blue", ls="--", label="hey")
axes[1].plot(y, x**3, color="red")

# Saving the figure as demonstrated in the notebook
fig4.savefig("My_graph.png")
plt.show()

# --- Exercise 5: Advanced Styling and Axis Limits ---
print("Rendering Exercise 5...")
fig5 = plt.figure()
ax5 = fig5.add_axes([0, 0, 1, 1])
ax5.plot(x, y, color="#FF8c00", linewidth=0.5, alpha=0.4, linestyle=":", 
         marker="o", markersize=3, markerfacecolor="green", markeredgewidth=3)
ax5.set_xlim(0, 1)
ax5.set_title("Advanced Styling & Limits")
plt.show()
