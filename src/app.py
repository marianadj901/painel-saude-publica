import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:postgres@db:5432/postgres")

query = """
SELECT 
    a.data, 
    a.diagnostico, 
    b.nome as bairro, 
    p.faixa_etaria
FROM atendimentos a
JOIN pacientes p ON a.paciente_id = p.paciente_id
JOIN bairros b ON a.bairro_id = b.bairro_id
"""

df = pd.read_sql(query, engine)

st.title("📊 Dashboard de Saúde")

st.dataframe(df)

# Análise de atendimentos por diagnóstico
st.subheader("📈 Atendimentos por diagnóstico")

grafico = df["diagnostico"].value_counts()
st.bar_chart(grafico)

# Análise de atendimentos por bairro
st.subheader("📍 Atendimentos por bairro")

grafico_bairro = df["bairro"].value_counts()
st.bar_chart(grafico_bairro)

#Filtro interativo por bairro
bairro_selecionado = st.selectbox("Escolha um bairro", df["bairro"].unique())

df_filtrado = df[df["bairro"] == bairro_selecionado]

st.dataframe(df_filtrado)

# Casos por dia
df["data"] = pd.to_datetime(df["data"])
casos_por_dia = df.groupby("data").size()

st.line_chart(casos_por_dia)

# Casos por faixa etária
faixa = df["faixa_etaria"].value_counts()
st.bar_chart(faixa)

# Interpretação dos dados
st.subheader("🧠 Insights")

st.write("""
- A doença mais frequente é: {}
- O bairro com mais atendimentos é: {}
""".format(
    df["diagnostico"].value_counts().idxmax(),
    df["bairro"].value_counts().idxmax()
))

#Métricas
col1, col2, col3 = st.columns(3)

col1.metric("Total de atendimentos", len(df))
col2.metric("Total de bairros", df["bairro"].nunique())
col3.metric("Doenças diferentes", df["diagnostico"].nunique())

#Filtros mais completos
diagnostico_sel = st.selectbox("Escolha um diagnóstico", df["diagnostico"].unique())

df_filtrado = df[
    (df["bairro"] == bairro_selecionado) &
    (df["diagnostico"] == diagnostico_sel)
]

st.dataframe(df_filtrado)

#Filtro por data
data_inicio = st.date_input("Data inicial", df["data"].min())
data_fim = st.date_input("Data final", df["data"].max())

df_filtrado = df[
    (df["data"] >= pd.to_datetime(data_inicio)) &
    (df["data"] <= pd.to_datetime(data_fim))
]

#Insights adicionais
st.write(f"""
### 📊 Insights automáticos

- Doença mais frequente: **{df["diagnostico"].value_counts().idxmax()}**
- Bairro com mais atendimentos: **{df["bairro"].value_counts().idxmax()}**
- Faixa etária mais afetada: **{df["faixa_etaria"].value_counts().idxmax()}**
""")

#Ordenar gráficos por frequência
grafico = df["diagnostico"].value_counts().sort_values(ascending=False)
st.bar_chart(grafico)

#Casos por faixa etária ordenados
faixa = df["faixa_etaria"].value_counts()
st.bar_chart(faixa)