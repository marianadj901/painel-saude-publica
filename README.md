# 🏥 Painel de Saúde Pública — AV2

<p align="center">
  <img src="src/dashboard.png" width="900">
</p>

<p align="center">
  Dashboard interativo para análise e previsão de atendimentos em saúde pública.
</p>

Projeto desenvolvido para as Avaliações 1 e 2 da disciplina de Ciência de Dados (NES).

O sistema simula dados de atendimentos de saúde pública, armazena-os em um banco de dados PostgreSQL, disponibiliza uma API REST construída com FastAPI e apresenta um dashboard interativo com análises descritivas e previsões utilizando Streamlit.

---

# 📋 Visão Geral

Este projeto implementa um **sistema de suporte à decisão** para análise de dados de saúde pública com:

- ✅ API intermediária desenvolvida com FastAPI
- ✅ Dashboard interativo em Streamlit
- ✅ Banco de dados PostgreSQL
- ✅ Consultas realizadas exclusivamente pela API
- ✅ Modelo preditivo integrado ao dashboard
- ✅ Arquitetura totalmente containerizada com Docker Compose

---

# 🏗️ Arquitetura

```text
┌─────────────────────────────────────────┐
│ Dashboard (Streamlit)                   │
│ • Indicadores                           │
│ • Gráficos                              │
│ • Filtros                               │
│ • Previsões                             │
└─────────────────┬───────────────────────┘
                  │ HTTP
                  ▼
┌─────────────────────────────────────────┐
│ API (FastAPI)                           │
│ • GET /health                           │
│ • GET /dados                            │
│ • GET /resumo                           │
└─────────────────┬───────────────────────┘
                  │ SQLAlchemy
                  ▼
┌─────────────────────────────────────────┐
│ Banco PostgreSQL                        │
│ Dados dos atendimentos                  │
└─────────────────────────────────────────┘
```

---

# 📡 Rotas da API

| Método | Endpoint | Descrição |
|---------|----------|-----------|
| GET | `/health` | Verifica se a API está funcionando |
| GET | `/dados` | Retorna os registros de atendimentos |
| GET | `/resumo` | Retorna estatísticas agregadas dos atendimentos |

## 📖 Documentação da API

Após iniciar o projeto, acesse:

```
http://localhost:8000/docs
```

A documentação Swagger é gerada automaticamente pelo FastAPI.

---

# 📊 Dashboard

O dashboard permite visualizar informações como:

- Total de atendimentos
- Casos por diagnóstico
- Casos por bairro
- Evolução diária dos atendimentos
- Distribuição por faixa etária
- Indicadores gerais
- Filtros interativos

Além disso, apresenta uma seção de previsão utilizando modelos de Machine Learning.

---

# 🤖 Modelo Preditivo

O dashboard possui um módulo de Machine Learning para previsão do número de atendimentos diários.

Modelos implementados:

- Regressão Linear
- Random Forest

O usuário pode:

- selecionar o modelo de previsão;
- definir a porcentagem dos dados destinada ao treinamento;
- visualizar a comparação entre valores reais e previstos;
- acompanhar as métricas de desempenho do modelo.

### Métricas apresentadas

- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)

---

# 📈 Resultados

Após a execução do projeto são gerados automaticamente dados simulados contendo aproximadamente:

- 200 atendimentos
- 50 pacientes
- 5 bairros
- 5 diagnósticos

O sistema executa corretamente:

- ✅ Banco PostgreSQL
- ✅ API FastAPI
- ✅ Dashboard Streamlit
- ✅ Comunicação entre Dashboard, API e Banco de Dados
- ✅ Execução completa utilizando Docker Compose

---

# 🛠️ Tecnologias Utilizadas

- Python 3.10
- FastAPI
- Streamlit
- PostgreSQL
- SQLAlchemy
- Pandas
- NumPy
- Scikit-Learn
- Docker
- Docker Compose

---

# ▶️ Como Executar

## Pré-requisitos

- Docker Desktop instalado
- Git instalado

### Clone o repositório

```bash
git clone https://github.com/marianadj901/painel-saude-publica.git
```

### Entre na pasta do projeto

```bash
cd painel-saude-publica-main
```

### Execute os containers

```bash
docker compose up --build
```

Após alguns segundos, os serviços estarão disponíveis.

---

# 🌐 Serviços

| Serviço | Endereço |
|----------|----------|
| Dashboard Streamlit | http://localhost:8501 |
| API FastAPI | http://localhost:8000 |
| Documentação Swagger | http://localhost:8000/docs |

---

# 📂 Estrutura do Projeto

```text
.
├── api/
│   ├── __init__.py
│   └── main.py
│
├── sql/
│   └── schema.sql
│
├── src/
│   ├── app.py
│   ├── db.py
│   ├── generate_data.py
│   └── modelo.py
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# 🎯 Objetivo

O objetivo deste projeto é fornecer uma ferramenta de apoio à decisão para análise de dados de saúde pública, permitindo visualizar indicadores, explorar tendências dos atendimentos e utilizar modelos preditivos para estimar a demanda futura.

---

# 👩‍💻 Desenvolvido para

**Disciplina:** Ciência de Dados (NES)

**Professor:** Eduardo Adame

**Projeto:** Avaliação 2 (AV2)

---

# 📄 Licença

Projeto desenvolvido exclusivamente para fins acadêmicos na disciplina de Ciência de Dados (NES).

---

# 📌 Observações

- A aplicação é totalmente executada via Docker Compose.
- O dashboard consome dados exclusivamente através da API FastAPI.
- A documentação interativa da API é gerada automaticamente pelo Swagger.
- O banco de dados é populado automaticamente com dados simulados durante a inicialização do projeto.
