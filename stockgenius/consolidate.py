import pandas as pd
import os

def consolidate_csv_files(data_dir):
    all_files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith('.csv')]
    df_list = [pd.read_csv(file) for file in all_files]
    consolidated_df = pd.concat(df_list, ignore_index=True)
    return consolidated_df