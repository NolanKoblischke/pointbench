import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('mystyle.mplstyle')

names = ['GPT-4o', 'Claude 3.5 Sonnet']
filenames = ['results/gpt4o.csv', 'results/claude35sonnet.csv']
points = pd.read_csv('points.csv')

# Plot 1: Predicted vs Actual Coordinates
fig, axes = plt.subplots(nrows=1, ncols=len(names), figsize=(11, 5))
fig.suptitle('Reading a Point off a Scatter Plot', y=0.87)

for idx, (name, filename) in enumerate(zip(names, filenames)):
    print('\n', name)
    model = pd.read_csv(filename)

    # Calculate the Euclidean distance between the actual and predicted points
    euclidean_distance = np.sqrt((model.x - points.x)**2 + (model.y - points.y)**2)
    print(f'Median Euclidean distance: {np.median(euclidean_distance):.2f}')
    threshold_for_correct_answer = 0.2
    N_correct = np.sum(euclidean_distance < threshold_for_correct_answer)
    ratio_correct = N_correct / len(euclidean_distance)
    print(f'Percentage of points within {threshold_for_correct_answer} units of the actual point: {ratio_correct:.1%}')

    ax = axes[idx]
    ax.scatter(points.x, model.x, label='x value')
    ax.scatter(points.y, model.y, label='y value')
    ax.set_xlabel('Actual Coordinate')
    if idx == 0:
        ax.set_ylabel('Predicted Coordinate')
    ax.plot([1, 9], [1, 9], color='black')
    ax.set_title(f'{name}')
    ax.text(3, 1, f'{ratio_correct:.0%} within {threshold_for_correct_answer} units', fontsize=16)

# Place legends outside the far rightmost plot
axes[-1].legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('analysis/predicted_vs_actual_coordinates.png', bbox_inches='tight')
plt.close()


# Plot 2: Predicted vs Actual with Lines
fig, axes = plt.subplots(nrows=1, ncols=len(names), figsize=(11, 5))
fig.suptitle('Predicted Point vs Actual Point', y=0.87)

for idx, (name, filename) in enumerate(zip(names, filenames)):
    model = pd.read_csv(filename)

    ax = axes[idx]
    ax.scatter(points.x, points.y, label='Actual')
    ax.scatter(model.x, model.y, label='Predicted')
    for i in range(len(points.x)):
        ax.plot([points.x[i], model.x[i]], [points.y[i], model.y[i]], color='black', alpha=0.2)
    ax.set_title(f'{name}')

# Place legends outside the far rightmost plot
axes[-1].legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('analysis/predicted_vs_actual_with_lines.png', bbox_inches='tight')
plt.close()


# Plot 3: Error Histogram
fig, axes = plt.subplots(nrows=1, ncols=len(names), figsize=(11, 5))
fig.suptitle('Error Histogram Per Axis', y=0.87)

for idx, (name, filename) in enumerate(zip(names, filenames)):
    model = pd.read_csv(filename)

    xerr = model.x - points.x
    yerr = model.y - points.y
    bins = np.linspace(min(xerr.min(), yerr.min()), max(xerr.max(), yerr.max()), 20)
    ax = axes[idx]
    ax.hist(xerr, bins=bins, alpha=0.5, label='x error')
    ax.hist(yerr, bins=bins, alpha=0.5, label='y error')    
    ax.axvline(0, color='black', lw=1, ls='--')
    ax.set_title(f'{name}')
    ax.set_xlabel('Predicted - Actual')
    if idx == 0:
        ax.set_ylabel('Frequency')
    print(f'Mean absolute x error: {np.mean(np.abs(model.x - points.x)):.2f}')
    print(f'Mean absolute y error: {np.mean(np.abs(model.y - points.y)):.2f}')
# Place legends outside the far rightmost plot
axes[-1].legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('analysis/error_histogram.png', bbox_inches='tight')
plt.close()