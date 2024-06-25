import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('mystyle.mplstyle')

names = ['GPT-4o', 'Claude 3.5 Sonnet']
filenames = ['results/gpt4o.csv', 'results/claude35sonnet.csv']

for name, filename in zip(names, filenames):
    print('\n', name)
    model = pd.read_csv(filename)
    points = pd.read_csv('points.csv')


    # Calculate the Euclidean distance between the actual and predicted points
    euclidean_distance = np.sqrt((model.x - points.x)**2 + (model.y - points.y)**2)
    print(f'Median Euclidean distance: {np.median(euclidean_distance):.2f}')
    threshold_for_correct_answer = 0.2
    N_correct = np.sum(euclidean_distance < threshold_for_correct_answer)
    ratio_correct = N_correct / len(euclidean_distance)
    print(f'Percentage of points within {threshold_for_correct_answer} units of the actual point: {ratio_correct:.1%}')

    # Plot predicted vs actual point
    plt.scatter(points.x, model.x, label='x value')
    plt.scatter(points.y, model.y, label='y value')
    plt.xlabel('Actual Coordinate')
    plt.ylabel('Predicted Coordinate')
    plt.plot([1,9],[1,9], color='black')
    plt.legend()
    plt.title(f'{name} reading a scatter plot')
    plt.text(5, 1, f'{ratio_correct:.0%} within {threshold_for_correct_answer} units', fontsize=16)
    plt.savefig(f'analysis/{name}_scatter.png', bbox_inches='tight')
    plt.close()

    # Plot predicted vs actual point and a line between them
    plt.scatter(points.x, points.y, label='Actual')
    plt.scatter(model.x, model.y, label='Predicted')
    for i in range(len(points.x)):
        plt.plot([points.x[i], model.x[i]], [points.y[i], model.y[i]], color='black', alpha=0.2)
    plt.title(f'{name} reading a scatter plot')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.savefig(f'analysis/{name}_scatter_with_lines.png', bbox_inches='tight')
    plt.close()

    # Plot histogram for x error and y error
    xerr = model.x - points.x
    yerr = model.y - points.y
    bins = np.linspace(min(xerr.min(), yerr.min()), max(xerr.max(), yerr.max()), 20)
    plt.hist(xerr, bins=bins, alpha=0.5, label='x error')
    plt.hist(yerr, bins=bins, alpha=0.5, label='y error')    
    plt.legend()
    plt.axvline(0, color='black')
    print(f'Mean absolute x error: {np.mean(np.abs(model.x - points.x)):.2f}')
    print(f'Mean absolute y error: {np.mean(np.abs(model.y - points.y)):.2f}')
    plt.title(f'{name} error histogram')
    plt.xlabel('Predicted Position - Actual Position')
    plt.ylabel('Frequency')
    plt.savefig(f'analysis/{name}_error_hist.png', bbox_inches='tight')
    plt.close()