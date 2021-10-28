import pandas as pd

with open('netflix.csv') as csvfile:
    read_csv = pd.read_csv(csvfile, sep=',', parse_dates=['date_added'], engine='python')
    composition = read_csv['type'].str.split(',', expand=True).stack().str.strip().reset_index(level=1, drop=True)
    composition = pd.DataFrame(composition,  columns=['type'],)

print(composition)