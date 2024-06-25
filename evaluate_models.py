import os
import importlib
import numpy as np
from tqdm import tqdm

# List of models to evaluate
models_to_evaluate = ['gpt4o', 'claude35sonnet']

# Main function to query models for existing plots
plots_dir = 'plots/'
results_dir = 'results/'
os.makedirs(results_dir, exist_ok=True)

# Assuming the plots are named 0.png, 1.png, ..., 99.png
for model_name in models_to_evaluate:
    
    module_name_with_prefix = f'models.{model_name}'
    model_module = importlib.import_module(module_name_with_prefix)

    prompt = "What is the position of this point? Output your answer in the format (x,y). E.g. (5.06,4.23). Be as precise as possible. Answer to 2 decimal places. These points are truly random so do not output whole numbers, try to use the decimals. Only output your answer in the format (x,y). Nothing else."

    csv_name = f'{results_dir}{model_name}_results.csv'
    with open(csv_name, 'w') as f:
        f.write('x,y\n')

    for i in tqdm(range(2)):
        plot_path = f'{plots_dir}{i}.png'

        try:
            response = model_module.get_position(image_path=plot_path,prompt=prompt)
            x, y = response.split(',')
            x = x.strip()[1:]
            y = y.strip()[:-1]
        except Exception as e:
            print(f'Error in getting position for plot {i} with {model_name}: {e}')
            x = np.nan
            y = np.nan
        with open(csv_name, 'a') as f:
            f.write(f'{x},{y}\n')
