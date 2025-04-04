import pandas as pd, sqlite3
from sqlalchemy import create_engine

def salvarCsv(df : pd.DataFrame, nome_arquivo : str, separador: str, decimal : str):
  df.to_csv(nome_arquivo, sep=separador, decimal=decimal)
  return

def salvarSQLite(df : pd.DataFrame, nome_banco : str, nome_tabela: str):
  """
  Criação da 
  """
  conn = sqlite3.connect(nome_banco) 

  df.to_sql(nome_tabela, conn, if_exists='replace', index=False)

  conn.close()
  return 

def salvarMySQL(
    df : pd.DataFrame, senha: str,  usuario : str, host : str, banco : str, nome_tabela : str
):
  engine = create_engine(f"mysql+pymysql://{usuario}:{senha}@{host}/{banco}")
  df.to_sql(nome_tabela, con=engine, if_exists='replace', index=False)
  return