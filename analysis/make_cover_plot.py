import numpy as np
import matplotlib.pyplot as plt

pt = [1.345, 4.379]

plt.figure(figsize=(8, 8))

# Plot all points
plt.plot(pt[0], pt[1], 'o', markersize=10, label='Point')
plt.plot(1.35, 4.4, 'x', markersize=6, color='red', markeredgewidth=2, label='My Guess')
plt.plot(1.40, 4.40, 'x', markersize=6, color='orange', markeredgewidth=2, label='Claude 3.5 Sonnet')
plt.plot(2.00, 4.00, 'x', markersize=6, color='purple', markeredgewidth=2, label='GPT-4o')

# Add a dashed blue circle around pt
circle = plt.Circle(pt, 0.2, fill=False, color='blue', linewidth=1.5, linestyle='--', label='0.2 Distance Threshold')
plt.gca().add_artist(circle)

# Add legend
plt.legend(loc='upper left', fontsize=14)

plt.title("What's the position of the point?", fontsize=20)
plt.xlim(0,10)
plt.ylim(0,10)
plt.minorticks_on()
plt.grid(which='both',linestyle='--')
plt.tight_layout()
plt.savefig('point_cover_plot.png')
plt.close()