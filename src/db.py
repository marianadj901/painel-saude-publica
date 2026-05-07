from sqlalchemy import create_engine

DB_USER = "user"
DB_PASSWORD = "password"
DB_HOST = "db"
DB_PORT = "5432"
DB_NAME = "saude"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@db:5432/saude"
)