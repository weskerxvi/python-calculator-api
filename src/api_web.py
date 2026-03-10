from fastapi import FastAPI
from api import resultado, Historico
import json

app = FastAPI()

@app.get("/")
def home(): 
    return {"message": "API da calculadora funcionando"}

@app.get("/calcular")
def calcular(operacao: int, valor1: float, valor2: float):
    res = resultado(operacao, valor1, valor2)

    return {
        "operacao": operacao,
        "valor1": valor1,
        "valor2": valor2,
        "resultado": res
    }

@app.get("/historico")
def historico():
    with open("resultados/historico.json", "r") as f:
        dados = json.load(f)

    return dados

@app.get("/ultima")
def ultima():
    return Historico.ultima_operacao()