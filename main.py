from src.extractTransform import requestApiBcb
from src.load import salvarCsv
import pandas as pd

dadosBcb = requestApiBcb('20191')
salvarCsv(dadosBcb, "src/datasets/meiosPagamentosTri.csv", ';', '.')
