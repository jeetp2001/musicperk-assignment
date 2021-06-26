import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

db = mysql.connector.connect(host='localhost',user='root',password='G0d!sgreat',database='first')

df = pd.read_sql('select * from trading',con = db)

df['SMA10'] = df['close'].rolling(10).mean()
df['SMA60'] = df['close'].rolling(60).mean()

print(df.tail())

df = df.dropna()

df = df[['close','SMA10','SMA60']]

buy = []
sell = []

for i in range(len(df)):
    if df.SMA10.iloc[i] > df.SMA60.iloc[i] and df.SMA10.iloc[i-1] < df.SMA60.iloc[i-1]:
        buy.append(i)

    elif df.SMA10.iloc[i] < df.SMA60.iloc[i] and df.SMA10.iloc[i-1] > df.SMA60.iloc[i-1]:
        sell.append(i)

plt.plot(df['close'],label='Asset price',c='blue',alpha=0.5)

plt.plot(df['SMA10'],label='SMA10',c='k',alpha=0.85)
plt.plot(df['SMA60'],label='SMA60',c='magenta',alpha=0.85)

plt.scatter(df.iloc[buy].index,df.iloc[buy]['close'],marker='^',color='g',s=100)
plt.scatter(df.iloc[sell].index,df.iloc[sell]['close'],marker='v',color='r',s=100)

plt.legend()
# plt.show()