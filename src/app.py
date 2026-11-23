from contextlib import asynccontextmanager
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, Request

from src.schemas import PassageiroRequest, PredictionResponse

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "modelo_mlp.joblib"

@asynccontextmanager
async def lifespan(app: FastAPI):
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"Modelo não encontrado em {MODEL_PATH}. Execute o notebook primeiro."
        )
    app.state.modelo = joblib.load(MODEL_PATH)
    yield
    app.state.modelo = None

app = FastAPI(
    title="API de Previsão de Sobrevivência no Titanic",
    description="API para realizar previsões com uma Rede Neural MLP.",
    version="1.0.0",
    lifespan=lifespan,
)

@app.get("/info")
async def info():
    return {
        "status": "ativo",
        "framework": "FastAPI",
        "modelo": "MLPClassifier"
    }

@app.post("/predict", response_model=PredictionResponse)
async def predict(dados: PassageiroRequest, request: Request):
    entrada = pd.DataFrame([dados.model_dump()])
    modelo = request.app.state.modelo

    classe = int(modelo.predict(entrada)[0])
    probabilidades = modelo.predict_proba(entrada)[0]
    probabilidade = float(probabilidades[classe])

    rotulos = {
        0: "Não sobreviveu",
        1: "Sobreviveu"
    }

    return PredictionResponse(
        classe_predita=rotulos[classe],
        probabilidade=probabilidade
    )
