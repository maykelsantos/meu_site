import pandas as pd
import matplotlib as plt
import requests
import json

url = 'https://apidatalake.tesouro.gov.br/ords/custos/tt/depreciacao'
response = requests.get(url)
data = response.json()
df = pd.DataFrame(pd.json_normalize(data))
print(df['items'][0][0])