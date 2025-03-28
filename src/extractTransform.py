import requests
import pandas as pd

#print(req.json())  #Deserialização (Transformar uma requisição em objeto python)

#df = pd.json_normalize(dados)  #Transformar em DataFrame #São mostradas todas as chaves
#df = pd.json_normalize(dados['value']) #Apenas a chave valor é mostrada


def requestApiBcb(data: str) -> pd.DataFrame:
  """
  Função para extrair os dados dos meios de pagamentos trimestrais do Banco Central.
  
  Parâmetros: 
  Data - String - aaaat (Exemplo: 20191)

  Saída:
  DataFrame - Estrutura de dados do Pandas.
  """
  url = f"https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre=%27{data}%27&$format=json"

  req = requests.get(url)
  dados = req.json()

  df = pd.json_normalize(dados['value'])
  df['datatrimestre'] = pd.to_datetime(df['datatrimestre'])
  return df

