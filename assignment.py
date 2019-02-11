import pandas as pd
mydataset=pd.read_csv('Reliance.csv')
x=mydataset.iloc[:,:].values
df=pd.DataFrame(x)
for row in x:
    if row[5]>25:
        row[6]=('increase')
    elif row[5]<25:
        row[6]=('decrease')
    else:
        row[6]=('no change')
df 
