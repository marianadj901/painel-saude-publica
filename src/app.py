from modelo import treinar_modelo
import streamlit as st
import pandas as pd
import requests

st.title("📊 Dashboard de Saúde")

# Filtros enviados para a API
bairro_filtro = st.text_input("Filtrar bairro")
diagnostico_filtro = st.text_input("Filtrar diagnóstico")

params = {}

if bairro_filtro:
    params["bairro"] = bairro_filtro

if diagnostico_filtro:
    params["diagnostico"] = diagnostico_filtro

dados = requests.get(
    "http://api:8000/dados",
    params=params
).json()

df = pd.DataFrame(dados)

# Evita erro quando não houver resultados
if df.empty:
    st.warning("Nenhum dado encontrado para os filtros selecionados.")
    st.stop()

st.dataframe(df)

# Análise de atendimentos por diagnóstico
st.subheader("📈 Atendimentos por diagnóstico")

grafico = df["diagnostico"].value_counts()
st.bar_chart(grafico)

# Análise de atendimentos por bairro
st.subheader("📍 Atendimentos por bairro")

grafico_bairro = df["bairro"].value_counts()
st.bar_chart(grafico_bairro)

# Filtro interativo por bairro
bairro_selecionado = st.selectbox(
    "Escolha um bairro",
    df["bairro"].unique()
)

df_filtrado = df[df["bairro"] == bairro_selecionado]

st.dataframe(df_filtrado)

# Casos por dia
df["data"] = pd.to_datetime(df["data"])
casos_por_dia = df.groupby("data").size()

st.subheader("🔮 Modelo Preditivo")

modelo_escolhido = st.selectbox(
    "Escolha o modelo",
    ["Regressão Linear", "Random Forest"]
)

t0 = st.slider(
    "Ponto de corte treino/teste",
    min_value=10,
    max_value=len(casos_por_dia)-5,
    value=int(len(casos_por_dia)*0.7)
)

y_real, y_prev, mae, rmse = treinar_modelo(
    casos_por_dia,
    modelo_escolhido,
    t0
)

col1, col2 = st.columns(2)

col1.metric("MAE", round(mae, 2))
col2.metric("RMSE", round(rmse, 2))

import matplotlib.pyplot as plt

st.subheader("📉 Comparação: valores reais x previsão")

fig, ax = plt.subplots()

ax.plot(y_real, label="Real")
ax.plot(y_prev, "--", label="Previsto")  # linha tracejada

ax.legend()

st.pyplot(fig)