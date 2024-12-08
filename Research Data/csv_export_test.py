import pandas as pd
import os
from pathlib import Path

data = pd.read_csv('Ns443-Durga-Expression-Test-Data.csv', low_memory=False)

file = os.getcwd() + "/Exports/research_data_pandas.csv"
filepath = Path(file)
filepath.parent.mkdir(parents=True, exist_ok=True)

data.to_csv(filepath)

