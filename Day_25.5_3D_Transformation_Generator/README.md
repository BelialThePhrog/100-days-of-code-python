# Vectorized 3D Transformation Engine

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![NumPy](https://img.shields.io/badge/NumPy-Optimized-green.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3D%20Plots-orange.svg)

## 📌 Project Overview
The **Vectorized 3D Transformation Engine** is a high-performance Python script designed to apply affine transformations (translation and rotation) to massive 3D point clouds. 

This project demonstrates the critical difference between standard iterative computing (Python `for` loops) and **hardware-accelerated vectorization** using linear algebra. By utilizing homogeneous coordinates and $4 \times 4$ transformation matrices, the script can compute combined spatial transformations for $10^6$ (one million) data points in a fraction of a second, entirely bypassing memory bottlenecks.

This approach is foundational for applications in Scientific Machine Learning (SciML), Finite Element Method (FEM) mesh manipulations, and Digital Twin simulations where large-scale spatial data processing is required.

## 🚀 Features
* **Massive Data Handling:** Generates and processes a synthetic dataset of 1,000,000 spatial coordinates $(x, y, z)$.
* **Homogeneous Coordinates:** Extends 3D vectors to 4D to allow simultaneous translation and rotation via a single matrix multiplication (dot product).
* **Zero-Loop Architecture:** Strictly relies on `numpy.matmul` for $O(1)$ Python overhead, delegating heavy computations to underlying C/Fortran BLAS libraries.
* **Performance Profiling:** Built-in benchmarking using `time.perf_counter()` to log exact execution speeds.
* **Safe Visualization:** Implements smart downsampling (rendering a 500-point subset) via Matplotlib to visualize mathematical transformations without crashing the rendering engine or overloading RAM.

## 🧮 Mathematical Foundation
Instead of calculating new positions point-by-point, the engine constructs a combined $4 \times 4$ transformation matrix:
1. **Rotation Matrix ($R_z$):** Rotates the space around the Z-axis by $\theta$ degrees.
2. **Translation Matrix ($T_{3D}$):** Shifts the space by a vector $[t_x, t_y, t_z]$.

The final position of the entire point cloud matrix ($N \times 4$) is calculated in a single vectorized step:
`Result = Point_Cloud @ (Translation @ Rotation)`

## 🛠️ How to Use

### Prerequisites
Ensure you have the required libraries installed:
```bash
pip install numpy matplotlib
```

### Installation
Clone the repository to your local machine:
```bash
git clone [https://github.com/BelialThePhrog/3D-Transformation-Engine.git](https://github.com/BelialThePhrog/3D-Transformation-Engine.git)
cd 3D-Transformation-Engine
```

### Execution
Run the script directly from the root directory:
```bash
python main.py
```

### Understanding the Inputs
During execution, the CLI will prompt you for specific transformation parameters:
* **`Degrees` (Rotation):** The angle (in degrees) by which the point cloud will be rotated around the Z-axis. Positive values result in counter-clockwise rotation.
* **`tx` (Translation X):** The distance to shift the entire dataset along the X-axis.
* **`ty` (Translation Y):** The distance to shift the dataset along the Y-axis.
* **`tz` (Translation Z):** The distance to shift the dataset along the Z-axis.

## 📊 Expected Output
1. **Terminal Log:** The script will output the preview of the newly transformed matrix alongside the exact time it took to perform the operation on 1,000,000 points.
2. **Interactive 3D Plot:** A Matplotlib window will open displaying a side-by-side comparison of the point cloud *before* and *after* the transformation. You can rotate and zoom the plots interactively to inspect the geometric changes.

## 💡 Engineering Takeaway
This project proves that understanding computer memory allocation and utilizing continuous memory blocks (NumPy arrays) is mandatory in data analytics. Attempting to process $N=10^9$ or even $N=10^6$ elements using standard Python object lists results in extreme memory swapping and performance death, whereas vectorized matrix operations resolve the same problem almost instantaneously.
