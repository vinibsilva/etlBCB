# **ETL BCB**

Este repositório contém as práticas do curso de Data Science, utilizando como base o conjunto de dados de estatísticas de pagamentos do Banco Central do Brasil.

A partir desse conjunto de dados, foi trabalhado o seguinte subrecurso:

## **Meios de Pagamento Trimestrais**

### **Descrição**

O conjunto de dados contém informações trimestrais sobre diferentes meios de pagamento no Brasil, incluindo transações realizadas via Pix, TED, DOC, boletos, cartões de crédito e débito, entre outros.

### **Funções utilizadas**

#### **requestApiBcb**
Função para extrair os dados dos meios de pagamentos trimestrais do Banco Central.
  
  Parâmetros: 
  Data - String - aaaat (Exemplo: 20191)

  Saída:
  DataFrame - Estrutura de dados do Pandas.

#### **salvarCsv**
Função para transformar o DataFrame, que foi gerado anteriormente, em um arquivo csv.
  
  Parâmetros: 
  Df - DataFrame
  nome_arquivo - String - Nome que o arquivo irá receber(também é possível especificar o diretório em que o mesmo será gerado)
  
  Separador - String
  
  Decimal - String - Formatação dos decimais (Ex: , ou .)

  Saída:
  Arquivo CSV.
### **Estrutura dos Dados**

#### **Valores Financeiros**

| **Nome**                   | **Tipo**  | **Título**                          | **Descrição**  |
|----------------------------|----------|-------------------------------------|---------------|
| `dataTrimestre`            | Texto    | Trimestre                           | Período trimestral da observação. |
| `valorPix`                 | Decimal  | Valor Pix                           | Volume financeiro (R$ milhões) das transações Pix liquidadas trimestralmente no SPI e fora do SPI, considerando ordens de pagamento e devoluções. |
| `valorTED`                 | Decimal  | Valor TED                           | Montante financeiro (R$ milhões) transferido por meio de TED (Transferência Eletrônica Direta) trimestralmente. |
| `valorTEC`                 | Decimal  | Valor TEC                           | Montante financeiro (R$ milhões) transferido trimestralmente por meio de TEC (Transferência Especial de Crédito). |
| `valorCheque`              | Decimal  | Valor Cheque                        | Montante financeiro (R$ milhões) de cheques interbancários e intrabancários compensados trimestralmente. |
| `valorBoleto`              | Decimal  | Valor Boleto                        | Montante financeiro (R$ milhões) de boletos interbancários e intrabancários compensados trimestralmente. |
| `valorDOC`                 | Decimal  | Valor DOC                           | Montante financeiro (R$ milhões) transferido trimestralmente por meio de DOC. |
| `valorCartaoCredito`       | Decimal  | Valor Cartão de Crédito             | Montante financeiro (R$ milhões) de transações realizadas com cartão de crédito trimestralmente. |
| `valorCartaoDebito`        | Decimal  | Valor Cartão de Débito              | Montante financeiro (R$ milhões) de transações realizadas com cartão de débito trimestralmente. |
| `valorCartaoPrePago`       | Decimal  | Valor Cartão Pré-pago               | Montante financeiro (R$ milhões) de transações realizadas com cartão pré-pago trimestralmente. |
| `valorTransIntrabancaria`  | Decimal  | Valor Transferência Intrabancária   | Montante financeiro (R$ milhões) de transferências realizadas trimestralmente entre contas de clientes da mesma instituição. |
| `valorConvenios`           | Decimal  | Valor Convênio                      | Montante financeiro (R$ milhões) referente a arrecadações trimestrais governamentais e não-governamentais. |
| `valorDebitoDireto`        | Decimal  | Valor Débito Direto                 | Montante financeiro (R$ milhões) trimestral referente a débitos previamente autorizados pelo cliente. |
| `valorSaques`              | Decimal  | Valor Saques                        | Montante financeiro (R$ milhões) de saques realizados em caixas eletrônicos trimestralmente. |

#### **Quantidade de Transações**

| **Nome**                      | **Tipo**  | **Título**                            | **Descrição**  |
|--------------------------------|----------|---------------------------------------|---------------|
| `quantidadePix`               | Decimal  | Quantidade Pix                        | Quantidade (em milhares) de transações Pix liquidadas trimestralmente. |
| `quantidadeTED`               | Decimal  | Quantidade TED                        | Quantidade (em milhares) de TEDs realizadas trimestralmente. |
| `quantidadeTEC`               | Decimal  | Quantidade TEC                        | Quantidade (em milhares) de TECs realizadas trimestralmente. |
| `quantidadeCheque`            | Decimal  | Quantidade Cheque                     | Quantidade (em milhares) de cheques compensados trimestralmente. |
| `quantidadeBoleto`            | Decimal  | Quantidade Boleto                     | Quantidade (em milhares) de boletos compensados trimestralmente. |
| `quantidadeDOC`               | Decimal  | Quantidade DOC                        | Quantidade (em milhares) de DOCs realizados trimestralmente. |
| `quantidadeCartaoCredito`     | Decimal  | Quantidade Cartão de Crédito          | Quantidade (em milhares) de transações com cartão de crédito. |
| `quantidadeCartaoDebito`      | Decimal  | Quantidade Cartão de Débito           | Quantidade (em milhares) de transações com cartão de débito. |
| `quantidadeCartaoPrePago`     | Decimal  | Quantidade Cartão Pré-pago            | Quantidade (em milhares) de transações com cartão pré-pago. |
| `quantidadeTransIntrabancaria`| Decimal  | Quantidade Transferência Intrabancária| Quantidade (em milhares) de transferências intrabancárias trimestrais. |
| `quantidadeConvenios`         | Decimal  | Quantidade Convênio                   | Quantidade (em milhares) de transações relacionadas a arrecadações trimestrais. |
| `quantidadeDebitoDireto`      | Decimal  | Quantidade Débito Direto              | Quantidade (em milhares) de transações de débitos diretos trimestrais. |
| `quantidadeSaques`            | Decimal  | Quantidade Saques                     | Quantidade (em milhares) de saques realizados trimestralmente. |





