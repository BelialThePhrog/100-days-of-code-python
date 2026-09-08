import matplotlib.pyplot as plt
import numpy as np

# Data Setup
x = np.arange(0, 100)
y = x * 2
z = x ** 2

# --- Exercise 1 ---
fig1 = plt.figure()
ax1 = fig1.add_axes([0, 0, 1, 1])
ax1.plot(x, y)
ax1.set_title("Exercise 1")
plt.show()

# --- Exercise 2 ---
fig2 = plt.figure()
ax2_main = fig2.add_axes([0, 0, 1, 1])
ax2_inset = fig2.add_axes([0.2, 0.5, 0.2, 0.2])

ax2_main.plot(x, y)
ax2_inset.plot(x, y)
ax2_main.set_title("Exercise 2 - Main")
ax2_inset.set_title("Exercise 2 - Inset")
plt.show()

# --- Exercise 3 ---
fig3 = plt.figure()
ax3_main = fig3.add_axes([0, 0, 1, 1])
ax3_inset = fig3.add_axes([0.2, 0.5, 0.4, 0.4])

ax3_main.plot(x, y)
ax3_inset.plot(x, z)
ax3_main.set_title("Exercise 3 - Main")
ax3_inset.set_title("Exercise 3 - Inset")
plt.show()

# --- Exercise 4 ---
fig4, axes4 = plt.subplots(nrows=1, ncols=2)
axes4[0].plot(x, y, color="blue", ls="--")
axes4[1].plot(x, z, color="red")
fig4.suptitle("Exercise 4")
plt.tight_layout()
plt.show()

# --- Exercise 4 (Resized) ---
fig5, axes5 = plt.subplots(nrows=1, ncols=2, figsize=(12, 2))
axes5[0].plot(x, y, color="blue", ls="--")
axes5[1].plot(x, z, color="red")
fig5.suptitle("Exercise 4 - Resized")
plt.tight_layout()
plt.show()
