import pandas as pd

df = pd.read_csv('AirPassengers.csv')
print(len(df['time']))
# print(df['time'])
# print(df['value'])

names = ['Wade', 'James', 'Kobe', 'Curry', 'Ben', 'Messi', 'Karaman']
total = [55, 50, 44, 36, 100, 91, 32]
data_set = list(zip(names, total))
print(names)
print(total)
print(data_set)
data_frame = pd.DataFrame(data=data_set, columns=['Names', 'Total'])
data_frame.to_csv('points', index=True, header=True)
data_frame.to_json('points.json', index=True)
df = pd.DataFrame(zip(names, total), columns=['Players', 'Total'])
with pd.ExcelWriter("points.xlsx") as writer:
    df.to_excel(writer)
print(data_frame.memory_usage())

papi = pd.read_excel('C:\\Users\\toaxo\\Desktop\\Sem5\\HPC\\Parallel_Programming\\Task2_PAPI\\PAPI_Data.xlsx',
                     keep_default_na=False, na_filter=False, sheet_name=0)
print(papi)
