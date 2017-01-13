import pandas as pd

df = pd.read_csv('covtype_preprocess.csv', index_col=0)
df_sample = df.sample(frac=0.001)

df_sample.to_csv('covtype_preprocess.sampled.csv')
