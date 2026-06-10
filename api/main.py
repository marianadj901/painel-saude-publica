from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd

app = FastAPI()

engine = create_engine(
    "postgresql://postgres:postgres@db:5432/saude"
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/dados")
def dados(
    bairro: str = None,
    diagnostico: str = None,
    data_inicio: str = None,
    data_fim: str = None
):

    query = """
    SELECT
        a.data,
        a.diagnostico,
        b.nome as bairro,
        p.faixa_etaria
    FROM atendimentos a
    JOIN pacientes p
        ON a.paciente_id = p.paciente_id
    JOIN bairros b
        ON a.bairro_id = b.bairro_id
    WHERE 1=1
    """

    params = {}

    if bairro:
        query += " AND b.nome = :bairro"
        params["bairro"] = bairro

    if diagnostico:
        query += " AND a.diagnostico = :diagnostico"
        params["diagnostico"] = diagnostico

    if data_inicio:
        query += " AND a.data >= :data_inicio"
        params["data_inicio"] = data_inicio

    if data_fim:
        query += " AND a.data <= :data_fim"
        params["data_fim"] = data_fim

    df = pd.read_sql(
        text(query),
        engine,
        params=params
    )

    return df.to_dict(orient="records")


@app.get("/resumo")
def resumo():

    query = """
    SELECT diagnostico
    FROM atendimentos
    """

    df = pd.read_sql(query, engine)

    return {
        "total_atendimentos": len(df),
        "diagnosticos": df["diagnostico"].nunique()
    }