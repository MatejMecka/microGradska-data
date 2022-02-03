import pandas as pd
from get_data import getData
import hashlib
from pathlib import Path
import datetime

date_to_parse = datetime.datetime.now() - datetime.timedelta(days=10)
date = f"{date_to_parse.day:02d}-{date_to_parse.month:02d}-{date_to_parse.year}"

teoretska = getData(date, 1)
poligon = getData(date, 2)
gradska = getData(date, 3)

dataset_names = ['teoretska', 'poligon', 'gradska']
datasets = [teoretska, poligon, gradska]

for ind, dataset in enumerate(datasets):
    try:
        df = pd.read_html(dataset) # this parses all the tables in webpages to a list
    except:
        print("Data does not exist")
        continue
    df = df[0]
    df = df.iloc[: , 1:]

    print(df.head())

    # Hash Candidates name
    df['Име, име на родител и презиме'] = df['Име, име на родител и презиме'].apply(
    lambda x: 
        hashlib.sha256(x.encode()).hexdigest()
    )

    filepath = f"data/{date}/{dataset_names[ind]}"
    Path(filepath).mkdir(parents=True, exist_ok=True)

    # Export as CSV and JSON
    df.to_csv(f"{filepath}/{dataset_names[ind]}.csv", index=False)
    df.to_json(f"{filepath}/{dataset_names[ind]}.json", orient="table")