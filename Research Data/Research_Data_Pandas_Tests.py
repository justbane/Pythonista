import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)

# Get the data
df = pd.read_csv("insurance.csv", parse_dates=True, low_memory=False)

print(df[df['sex'] == 'female'].groupby('region')['sex'].count()['southeast'], df[df['sex'] == 'male'].groupby('region')['sex'].count()['southeast'])

plt.show()
