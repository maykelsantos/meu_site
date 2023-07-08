print('Importação das bibliotecas necessárias')

import pandas as pd
import plotly_express as px
import requests

print('Validação da requisição')

url = 'https://dadosabertos.camara.leg.br/api/v2/deputados'
response = requests.get(url)

print('Conversão para DataFrame')

data = response.json()
df = pd.json_normalize(data['dados'])

print('Remoção das colunas desnecessárias')

df = df.drop(['uri', 'uriPartido', 'idLegislatura', 'urlFoto'], axis = 1)

print('Plotagem do gráfico')

fig = px.bar(df.groupby(['siglaUf']).count().reset_index(),
             x = 'siglaUf',
             y = 'id',
             labels = {
                 'siglaUf': '',
                 'id': ''
                 })
print('Update do gráfico')

print('Conversão do gráfico para HTML')

fig.write_html('J:/Meu Drive/repos/meu_site/venv/html/graficos/total_deputado_estado.html')

print('Concluído!')