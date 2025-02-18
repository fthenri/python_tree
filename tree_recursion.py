import matplotlib.pyplot as plt
import numpy as np

def draw_branch(x, y, length, angle, thickness, depth, ax):
    if depth == 0:  
        return

    x_new = x + length * np.cos(np.radians(angle))
    y_new = y + length * np.sin(np.radians(angle))

    ax.plot([x, x_new], [y, y_new], color="black", linewidth=thickness)

    new_length = length * np.random.uniform(0.7, 0.9)
    new_thickness = max(thickness * 0.7, 0.1)

    angle_variation = np.random.uniform(10, 20)
    
    draw_branch(x_new, y_new, new_length, angle + angle_variation, new_thickness, depth - 1, ax)
    draw_branch(x_new, y_new, new_length, angle - angle_variation, new_thickness, depth - 1, ax)

fig, ax = plt.subplots(figsize=(12, 16))
ax.set_xlim(-50, 50)
ax.set_ylim(0, 100)
ax.axis("off")

draw_branch(-20, -20, length=10, angle=60, thickness=5, depth=11, ax=ax)

plt.show()
