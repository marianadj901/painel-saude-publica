import time
import random
from datetime import datetime, timedelta
from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql://postgres:postgres@db:5432/saude"
)

for i in range(15):
    try:
        with engine.connect() as conn:
            print("Banco conectado!")
            break
    except Exception:
        print(f"Aguardando banco... tentativa {i+1}/15")
        time.sleep(2)

with engine.connect() as conn:

    print("🔧 Criando tabelas...")

    # Criar tabelas
    conn.execute(text("""
    CREATE TABLE IF NOT EXISTS pacientes (
        paciente_id SERIAL PRIMARY KEY,
        faixa_etaria VARCHAR(20)
    );
    """))

    conn.execute(text("""
    CREATE TABLE IF NOT EXISTS bairros (
        bairro_id SERIAL PRIMARY KEY,
        nome VARCHAR(50)
    );
    """))

    conn.execute(text("""
    CREATE TABLE IF NOT EXISTS atendimentos (
        atendimento_id SERIAL PRIMARY KEY,
        data DATE,
        diagnostico VARCHAR(50),
        paciente_id INT,
        bairro_id INT,
        FOREIGN KEY (paciente_id) REFERENCES pacientes(paciente_id),
        FOREIGN KEY (bairro_id) REFERENCES bairros(bairro_id)
    );
    """))

    print("✅ Tabelas criadas!")

    print("🧹 Limpando dados antigos...")

    # Limpar dados (pra não duplicar)
    conn.execute(text("DELETE FROM atendimentos"))
    conn.execute(text("DELETE FROM pacientes"))
    conn.execute(text("DELETE FROM bairros"))

    # Resetar IDs
    conn.execute(text("ALTER SEQUENCE pacientes_paciente_id_seq RESTART WITH 1"))
    conn.execute(text("ALTER SEQUENCE bairros_bairro_id_seq RESTART WITH 1"))
    conn.execute(text("ALTER SEQUENCE atendimentos_atendimento_id_seq RESTART WITH 1"))

    print("✅ Banco limpo!")

    print("📍 Inserindo bairros...")

    bairros = ["Centro", "Zona Norte", "Zona Sul", "Zona Leste", "Zona Oeste"]

    for b in bairros:
        conn.execute(text("INSERT INTO bairros (nome) VALUES (:nome)"), {"nome": b})

    print("👥 Inserindo pacientes...")

    faixas = ["0-18", "19-30", "31-50", "51+"]

    # Criar 50 pacientes
    for _ in range(50):
        faixa = random.choice(faixas)
        conn.execute(
            text("INSERT INTO pacientes (faixa_etaria) VALUES (:faixa)"),
            {"faixa": faixa}
        )

    print("🏥 Gerando atendimentos...")

    diagnosticos = ["Gripe", "Covid", "Dengue", "Zika", "Chikungunya"]

    data_inicial = datetime(2024, 1, 1)

    # Gerar 200 atendimentos
    for _ in range(200):
        data = data_inicial + timedelta(days=random.randint(0, 60))
        diagnostico = random.choice(diagnosticos)
        paciente_id = random.randint(1, 50)
        bairro_id = random.randint(1, len(bairros))

        conn.execute(text("""
            INSERT INTO atendimentos (data, diagnostico, paciente_id, bairro_id)
            VALUES (:data, :diagnostico, :paciente_id, :bairro_id)
        """), {
            "data": data,
            "diagnostico": diagnostico,
            "paciente_id": paciente_id,
            "bairro_id": bairro_id
        })

    conn.commit()

    print("✅ Dados inseridos com sucesso!")
