import matplotlib.pyplot as plt
import numpy as np
import os

# --- FINAL REAL DATA (From your run_pipeline.py) ---
datasets = ['FD001', 'FD002', 'FD003', 'FD004']

# Exact values you obtained
rmse_linear = [32.04, 33.94, 57.08, 47.76]
rmse_rf =     [17.21, 17.98, 20.08, 20.28]
rmse_svr =    [19.31, 30.04, 21.40, 36.33]
rmse_lstm =   [14.49, 16.61, 13.77, 20.91]  

x = np.arange(len(datasets))
width = 0.20 

plt.figure(figsize=(12, 7))

# Create the bars
plt.bar(x - 1.5*width, rmse_linear, width, label='1. Linear (Baseline)', color='#ff9999', edgecolor='grey')
plt.bar(x - 0.5*width, rmse_svr,    width, label='2. SVR (SVM)',         color='#ffd700', edgecolor='grey')
plt.bar(x + 0.5*width, rmse_rf,     width, label='3. Random Forest',     color='#87cefa', edgecolor='grey')
plt.bar(x + 1.5*width, rmse_lstm,   width, label='4. LSTM (Deep Learning)', color='#3cb371', edgecolor='grey')

# Styling / Decoration
plt.xlabel('Dataset (Complexity)', fontsize=12, fontweight='bold')
plt.ylabel('RMSE (Cycles) - Lower is better', fontsize=12, fontweight='bold')
plt.title('Final Results: Performance Comparison', fontsize=14)
plt.xticks(x, ['FD001\n(Simple)', 'FD002\n(6 Conditions)', 'FD003\n(2 Faults)', 'FD004\n(Complex)'], fontsize=11)
plt.legend(fontsize=10, loc='upper left')
plt.grid(axis='y', linestyle='--', alpha=0.4)

# Highlight the WINNER of each dataset
all_results = [rmse_linear, rmse_svr, rmse_rf, rmse_lstm]
offsets = [-1.5, -0.5, 0.5, 1.5]

for i in range(len(datasets)):
    # Find the lowest value (best) in this dataset
    values = [model[i] for model in all_results]
    best_val = min(values)
    best_idx = values.index(best_val)
    
    # Write the value on top of the winning bar
    plt.text(i + offsets[best_idx]*width, best_val + 0.5, f"{best_val:.1f}", 
             ha='center', fontweight='bold', color='black')

plt.tight_layout()

# Save
save_dir = '../docs/figures'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
plt.savefig(f'{save_dir}/final_comparison_chart.png', dpi=300)
plt.show()