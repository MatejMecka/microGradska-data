from os import listdir, rmdir, mkdir
from shutil import rmtree
import pandas as pd

# Summarizied datasets
FOLDER_NAME = 'summary'
SUMMARY_FILE_NAMES = ['gradska.csv', 'teoretska.csv', 'poligon.csv']
rmtree(FOLDER_NAME, ignore_errors=True)
mkdir(FOLDER_NAME)

# Create Files

[pd.DataFrame(list()).to_csv(f'summary/{file_name}') for file_name in SUMMARY_FILE_NAMES ]

# Loop Through Dates
dates = [f for f in listdir('data')]

# Loop Through Categories
categories = [[elem for elem in listdir(f"data/{date}")] for date in dates]

for ind, category_list in enumerate(categories):
    summarized_datasets = {"gradska": pd.read_csv('summary/gradska.csv', index_col=False), "teoretska": pd.read_csv('summary/teoretska.csv', index_col=False), "poligon": pd.read_csv('summary/poligon.csv', index_col=False)}
    for category in category_list:
     file = pd.read_csv(f"data/{dates[ind]}/{category}/{category}.csv")
     file['date'] = pd.to_datetime(dates[ind], dayfirst=True)
     pd.concat([summarized_datasets[category], file]).to_csv(f'summary/{category}.csv', index=False)
    
