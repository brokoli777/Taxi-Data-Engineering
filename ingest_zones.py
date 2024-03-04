
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

    csv_name = 'zone-data.csv'
    os.system(f'wget  {url} -O {csv_name}')

    # df = pd.read_csv('yellow_tripdata_2021-01.csv', nrows=100)
    # df.tpep_pickup_datetime = pd.to_datetime(df['tpep_pickup_datetime'])
    # df.tpep_dropoff_datetime = pd.to_datetime(df['tpep_dropoff_datetime'])

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

    engine.connect()

    df = pd.read_csv('zone-data.csv')

    df.to_sql(name=table_name, con=engine, if_exists='append')

    


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

