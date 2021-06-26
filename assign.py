import pandas as pd
import sqlalchemy 

user = 'root'
host = 'localhost'
database = 'first'
password = 'G0d!sgreat'


df = pd.read_excel('HINDALCO_1D.xls')
print(df.head())

dbcon = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(user,password,host,database))

df.to_sql(con = dbcon,name='trading')
