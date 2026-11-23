# AT2 – Redes Neurais MLP

## Sobre o projeto

Este trabalho utiliza uma rede neural MLP para fazer previsões sobre a sobrevivência de passageiros do Titanic. O modelo recebe algumas informações do passageiro, como classe da passagem, idade, sexo e tarifa, e prevê uma das duas possibilidades: sobreviveu ou não sobreviveu.

## Dataset

O arquivo utilizado é o `train.csv`, disponível na competição Titanic do Kaggle:
https://www.kaggle.com/competitions/titanic/data

Depois de baixar o arquivo, coloque-o na pasta `data`, mantendo o nome `train.csv`. O arquivo não está incluído neste projeto e precisa ser baixado separadamente.

## 1. Preparar o ambiente

É necessário ter Python 3.11 ou superior e UV instalados. Abra a pasta do projeto no VS Code e abra o terminal em **Terminal > New Terminal**. Execute:

```powershell
uv sync
```

## 2. Executar o notebook

Abra `notebooks/analise_treinamento.ipynb` no VS Code. Se necessário, instale as extensões Python e Jupyter. Selecione o ambiente Python do projeto e execute as células na ordem.

O notebook faz a leitura dos dados, mostra algumas informações do dataset, prepara as colunas, treina o modelo e apresenta as métricas de avaliação. Ao final, o modelo é salvo em `models/modelo_mlp.joblib`.

## 3. Iniciar a API

Depois de executar o notebook e gerar o arquivo do modelo, volte ao terminal, na pasta principal do projeto, e execute:

```powershell
uv run fastapi dev src/app.py
```

A documentação da API pode ser acessada em:
http://127.0.0.1:8000/docs

## 4. Testar a API

O arquivo `requisicoes.http` contém exemplos para testar as rotas. Para executá-los pelo VS Code, instale a extensão REST Client e abra esse arquivo.

As rotas são:

- `GET /info`: mostra informações básicas da API.
- `POST /predict`: recebe os dados de um passageiro e retorna a previsão.

Também há uma requisição com idade inválida. Nesse caso, a API deve responder com o código HTTP 422, indicando que os dados enviados não passaram pela validação.

## Organização das pastas

```text
am-at2-redes-neurais/
├── data/
│   └── train.csv
├── models/
│   └── modelo_mlp.joblib
├── notebooks/
│   └── analise_treinamento.ipynb
├── src/
│   ├── __init__.py
│   ├── app.py
│   └── schemas.py
├── pyproject.toml
├── requisicoes.http
└── README.md
```

O arquivo `train.csv` deve ser colocado na pasta `data`. O arquivo `modelo_mlp.joblib` será criado quando o notebook for executado.
