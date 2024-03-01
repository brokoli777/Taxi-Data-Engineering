
import pandas as pd
from pandas.io import sql
from sqlalchemy import create_engine

import argparse

pd.__version__

parser = argparse.ArgumentParser(description='Ingest CSV into Postgre Database')



parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))


df = pd.read_csv('yellow_tripdata_2021-01.csv', nrows=100)

df.tpep_pickup_datetime = pd.to_datetime(df['tpep_pickup_datetime'])


df.tpep_dropoff_datetime = pd.to_datetime(df['tpep_dropoff_datetime'])


engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')


engine.connect()


print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))



df_iter = pd.read_csv('yellow_tripdata_2021-01.csv', iterator=True, chunksize=100000)


df = next(df_iter)


len(df)


df.tpep_pickup_datetime = pd.to_datetime(df['tpep_pickup_datetime'])
df.tpep_dropoff_datetime = pd.to_datetime(df['tpep_dropoff_datetime'])


df.head(n=0).to_sql('yellow_taxi_data', con=engine, if_exists='replace')


df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')


while True:
    try:
        df = next(df_iter)
        df.tpep_pickup_datetime = pd.to_datetime(df['tpep_pickup_datetime'])
        df.tpep_dropoff_datetime = pd.to_datetime(df['tpep_dropoff_datetime'])
        %time df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')
    except StopIteration:
        break




