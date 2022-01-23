import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine("mysql+pymysql://root:@localhost/test_db?charset=utf8mb4")

print(pd.read_sql('overview', engine))