import pandas as pd
data_g = pd.read_csv('/Users/gloriarumao/OneDrive - stevens.edu/python/webscrapenames')
data_j = pd.read_csv('/Users/gloriarumao/OneDrive - stevens.edu/python/webscrapenames 2')
data_a = pd.read_csv('Fontes_companyInfo.txt', delimiter = "\t")
data_af = data_a.rename(columns={'0': 'Name', '1': 'Purpose'})
data_s = pd.read_csv('3c.csv')
data_sp = data_s.rename(columns={'name': 'Name', 'purpose': 'Purpose'})
frames = [data_g, data_j, data_af, data_sp]
df = pd.concat(frames, ignore_index=True)

print(df.shape[0])
print(df)