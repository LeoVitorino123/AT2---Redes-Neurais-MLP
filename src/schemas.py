from pydantic import BaseModel, Field, ConfigDict
from typing import Literal

class PassageiroRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    Pclass: int = Field(ge=1, le=3, description="Classe do passageiro: 1, 2 ou 3", examples=[3])
    Sex: Literal["male", "female"] = Field(description="Sexo registrado no dataset", examples=["female"])
    Age: float = Field(ge=0, le=100, description="Idade em anos", examples=[25.0])
    SibSp: int = Field(ge=0, le=8, description="Número de irmãos/cônjuges a bordo", examples=[0])
    Parch: int = Field(ge=0, le=6, description="Número de pais/filhos a bordo", examples=[0])
    Fare: float = Field(ge=0, le=600, description="Tarifa paga", examples=[32.5])
    Embarked: Literal["C", "Q", "S"] = Field(description="Porto de embarque: C, Q ou S", examples=["S"])

class PredictionResponse(BaseModel):
    classe_predita: str
    probabilidade: float = Field(ge=0.0, le=1.0)
