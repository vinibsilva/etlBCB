import pandas as pd

def salvarCsv(df : pd.DataFrame, nome_arquivo : str, separador: str, decimal : str):
  """Função para transformar o DataFrame, que foi gerado anteriormente, em um arquivo csv.
  
  Parâmetros: 
  Df - DataFrame
  nome_arquivo - String - Nome que o arquivo irá receber(também é possível especificar o diretório em que o mesmo será gerado)
  Separador - String
  Decimal - String - Formatação dos decimais (Ex: , ou .)

  Saída:
  Arquivo CSV."""
  df.to_csv(nome_arquivo, sep=separador, decimal=decimal)
  return
