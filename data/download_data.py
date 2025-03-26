import requests

url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2021-01.parquet'
response = requests.get(url)

with open('green_tripdata_2021-01.parquet', 'wb') as file:
    file.write(response.content)
file.close()