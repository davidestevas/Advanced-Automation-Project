# Content for code/data/make_dataset.py
import pandas as pd

def load_and_clean_data(file_id, base_path='../data'):
    """
    Reusable function to load and clean C-MAPSS data.
    """
    # Column names
    index_names = ['unit_nr', 'time_cycles']
    setting_names = ['setting_1', 'setting_2', 'setting_3']
    sensor_names = ['s_{}'.format(i) for i in range(1, 22)] 
    col_names = index_names + setting_names + sensor_names

    # Load data
    try:
        train = pd.read_csv(f'{base_path}/raw/train_{file_id}.txt', sep='\s+', header=None, names=col_names)
        test = pd.read_csv(f'{base_path}/raw/test_{file_id}.txt', sep='\s+', header=None, names=col_names)
        rul = pd.read_csv(f'{base_path}/raw/RUL_{file_id}.txt', header=None, names=['RUL_actual'])
    except FileNotFoundError:
        print(f"Error: File {file_id} not found.")
        return None, None, None

    # Calculate RUL in training
    max_cycle = train.groupby('unit_nr')['time_cycles'].max().reset_index()
    max_cycle.columns = ['unit_nr', 'max_cycle']
    train = train.merge(max_cycle, on='unit_nr', how='left')
    train['RUL'] = train['max_cycle'] - train['time_cycles']
    train.drop('max_cycle', axis=1, inplace=True)
    
    return train, test, rul
