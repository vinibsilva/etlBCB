from src.extractTransform import requestApiBcb
from src.load import salvarCsv, salvarSQLite, salvarMySQL
import pandas as pd

dadosBcb = requestApiBcb('20191')
# salvarCsv(dadosBcb, "etlBCB/src/datasets/meiosPagamentosTri.csv", ';', '.')

# salvarSQLite(dadosBcb, "etlBCB/src/datasets/etlbcb.db", "meios_pagamentos_tri")

salvarMySQL(dadosBcb, 'teste', 'root', 'localhost', 'etlbcb', 'meios_pagamentos_tri')