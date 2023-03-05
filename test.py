from sqlalchemy import create_engine
import pandas as pd

username = 'root'
password = 'codehunter92586400'
port = '3306'
hostname = '127.0.0.1'
schema_name = 'dw_bi'

#print("mysql+pymysql://"+username+":"+password+"@"+hostname+":"+port+"/"+schema_name)
engine = create_engine("mysql+pymysql://"+username+":"+password+"@"+hostname+":"+port+"/"+schema_name)

sql = "SELECT id, tabela,tipo,modulo,sequencia,string_del,string_ins FROM dw_bi.queries  WHERE db_origem = 'ORACLE'  and id = 11 AND tipo = 'D' order by tipo asc,sequencia asc;"
data=pd.read_sql(sql,engine)

print(data)
