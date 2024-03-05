import pyarrow.parquet as pq
import pandas as pd
#parquet_file = pq.ParquetFile('yellow_tripdata_2023-12.parquet')

# for i in parquet_file.iter_batches(batch_size=100000):
#     # print("RecordBatch")
#     print(i.to_pandas())

df = pd.read_parquet('yellow_tripdata_2023-12.parquet')

# Extract the column names (header row)
header_row = df.columns.tolist()

print("Header Row:", header_row)

