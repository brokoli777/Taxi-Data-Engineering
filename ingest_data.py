
import pandas as pd
from pandas.io import sql
from sqlalchemy import create_engine
import argparse
import os
import pyarrow.parquet as pq

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    parquet_name = 'taxi-data.parquet'
    os.system(f'wget  {url} -O {parquet_name}')

    # df = pd.read_csv('yellow_tripdata_2021-01.csv', nrows=100)
    # df.tpep_pickup_datetime = pd.to_datetime(df['tpep_pickup_datetime'])
    # df.tpep_dropoff_datetime = pd.to_datetime(df['tpep_dropoff_datetime'])

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

    engine.connect()

    # df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)

    # df = next(df_iter)

    # len(df)

    # df.tpep_pickup_datetime = pd.to_datetime(df['tpep_pickup_datetime'])
    # df.tpep_dropoff_datetime = pd.to_datetime(df['tpep_dropoff_datetime'])

    # df.head(n=0).to_sql(table_name, con=engine, if_exists='replace')

    # df.to_sql(name=table_name, con=engine, if_exists='append')

    # while True:
    #     try:
    #         df = next(df_iter)
    #         df.tpep_pickup_datetime = pd.to_datetime(df['tpep_pickup_datetime'])
    #         df.tpep_dropoff_datetime = pd.to_datetime(df['tpep_dropoff_datetime'])
    #         df.to_sql(name=table_name, con=engine, if_exists='append')
    #     except StopIteration:
    #         break

    parquet_file = pq.ParquetFile(parquet_name)

    for i in parquet_file.iter_batches(batch_size=100000):
        # print("RecordBatch")
        # print(i.to_pandas())
        df = i.to_pandas()
        df.tpep_pickup_datetime = pd.to_datetime(df['tpep_pickup_datetime'])
        df.tpep_dropoff_datetime = pd.to_datetime(df['tpep_dropoff_datetime'])
        df.to_sql(name=table_name, con=engine, if_exists='replace')
        print("Batch inserted")


if __name__ == '__main__':
    pd.__version__
    parser = argparse.ArgumentParser(description='Ingest CSV into Postgre Database')

    parser.add_argument('--user', help='Postgres user name')
    parser.add_argument('--password', help='Postgres password')
    parser.add_argument('--host', help='Postgres host')
    parser.add_argument('--port', help='Postgres port')
    parser.add_argument('--db', help='Postgres database name')
    parser.add_argument('--table_name', help='name of table where data is to be stored')
    parser.add_argument('--url', help='url of csv file')

    args = parser.parse_args()

    main(args)

