# Artificial Skin Deformation Modeling (Cauchy Strain Tensor)

## 🧠 Project Overview
This is a mathematical mini-project focused on computational biomechanics and continuum mechanics. The goal is to simulate and visualize the deformation of an artificial skin sample by computing the **Cauchy Strain Tensor** ($\epsilon$) based on nodal displacements in both 2D (Quad-4 elements) and 3D (Hexahedron-8 elements). 

By defining custom displacement vectors, the model effectively demonstrates fundamental physical behaviors such as longitudinal stretching, transverse compression, and Z-axis thinning (Poisson's effect).
## 🤖 AI-Assisted Learning Disclaimer
**Transparency Note:** The Python code (`numpy` matrix operations and `matplotlib` 3D visualizations) in this repository was generated using AI tools. 

My primary role in this project was that of a **learner and mathematical architect**. I utilized AI as an interactive tutor to translate complex mathematical formulas (like the Jacobian matrix inversion and shape function derivatives) into code[cite: 24]. This allowed me to focus my energy strictly on understanding the underlying physics, tensor calculus, and the principles of the Finite Element Method (FEM), rather than typing boilerplate syntax.

## 🧮 Mathematical Concepts Explored
*   **Finite Element Method (FEM / MES):** Utilizing shape functions and natural coordinate systems ($\xi, \eta, \zeta$) to map local deformations to a global coordinate space.
*   **Jacobian Matrix:** Computing the transformation matrix between the natural and global coordinate systems.
*   **Cauchy Strain Tensor:** Calculating the symmetric strain tensor using the displacement gradient: 
    $$ \epsilon = \frac{1}{2}(\nabla u + (\nabla u)^T) $$
*   **Biomechanics:** Observing real-world physical reactions in artificial skin, such as how an extension in the X-axis by 15% results in a proportional thinning in the Y and Z axes by 4%.

## How to Run
Run the Python script directly. You can modify the `u` (displacement) array inside the script to test different physical forces like pure shear, rotation, or uniaxial stretching.

    python skin_tensor_model.py
