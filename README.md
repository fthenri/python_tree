# 🌳 Realistic Tree Branches with Python

## 📌 Introduction
This project generates a **realistic tree** using Python, leveraging **Matplotlib** for visualization and **NumPy** for mathematical calculations. The tree grows recursively, with branches that become **thinner**, **shorter**, and **vary in angle**, creating a natural look.

## 🛠️ Requirements
Make sure you have the following libraries installed:
```bash
pip install matplotlib numpy
```

## 🚀 How It Works
The tree is generated using a recursive function called draw_branch, which follows these principles:

1. Recursive Growth: The function calls itself twice to create two new branches.
2. Branch Slimming: As branches extend, they reduce in thickness.
3. Length Reduction: Each new branch is shorter than its parent.
4. Randomized Angles: Adds slight variation to each new branch angle for a more organic feel.
   
## 📜 Code Explanation

### 1️⃣ Import Required Libraries
```bash
import matplotlib.pyplot as plt
import numpy as np
```
- Matplotlib: Used to plot the tree.
- NumPy: Helps with angle calculations and randomness.
  
### 2️⃣ Recursive Function to Draw Branches
```bash
def draw_branch(x, y, length, angle, thickness, depth, ax):
    if depth == 0:  # Base case: stop recursion when depth reaches 0
        return
```
- If depth reaches zero, the recursion stops (prevents infinite looping).
  
### 3️⃣ Calculate New Branch Coordinates
```bash
    x_new = x + length * np.cos(np.radians(angle))
    y_new = y + length * np.sin(np.radians(angle))
```
- Uses trigonometry to calculate the new branch endpoint (x_new, y_new).
- Converts angle from degrees to radians because NumPy uses radians.
  
### 4️⃣ Draw the Branch
```bash
    ax.plot([x, x_new], [y, y_new], color="brown", linewidth=thickness)
```
- Plots a line from (x, y) to (x_new, y_new) with a brown color (to mimic tree bark).
- The thickness decreases as branches grow.
  
### 5️⃣ Decrease Length & Thickness for Next Branches
```bash
    new_length = length * np.random.uniform(0.7, 0.9)
    new_thickness = max(thickness * 0.7, 0.5)
```
- New branch length is randomly reduced between 70% and 90% of the current length.
- New thickness reduces to 70% of the previous branch but is never below 0.5.

### 6️⃣ Generate New Angles with Slight Randomness
```bash
    angle_variation = np.random.uniform(10, 20)
```
- Each new branch will randomly vary its angle between 10° and 20°.

### 7️⃣ Recursively Create Left and Right Branches
```bash
    draw_branch(x_new, y_new, new_length, angle + angle_variation, new_thickness, depth - 1, ax)
    draw_branch(x_new, y_new, new_length, angle - angle_variation, new_thickness, depth - 1, ax)
```
- Each branch splits into two:
- One angles up (+angle_variation).
- One angles down (-angle_variation).
- This continues recursively until depth = 0.

### 8️⃣ Set Up the Plot and Draw the Tree
```bash
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_xlim(-50, 50)
ax.set_ylim(0, 100)
ax.axis("off")
```
- Creates a Matplotlib figure with a size of 6x8 inches.
- Sets axis limits so branches don't go out of bounds.
- Removes axis labels to keep the image clean.

### 9️⃣ Call the Function to Draw the First Branch
```bash
draw_branch(0, 0, length=30, angle=90, thickness=5, depth=10, ax)
```
- Starts from the trunk base (0,0).
- Initial branch is 30 units long, 5 units thick.
- depth=10 means the recursion will run 10 times.
  
### 🔟 Display the Tree
```bash
plt.show()
```
- Renders the generated tree!

## 🎨 Example Output
- Running the script will produce a tree-like structure with natural branch variation.
