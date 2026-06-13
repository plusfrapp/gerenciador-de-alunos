import sqlite3
import os
import threading

# Caminhos baseados na localização deste arquivo
_PASTA_DB  = os.path.dirname(os.path.abspath(__file__))
SCHEMA_PATH = os.path.join(_PASTA_DB, 'schema.sql')
DB_PATH     = os.path.join(os.path.dirname(_PASTA_DB), 'escola.db')

# Uma conexão por thread (evita abrir/fechar a cada operação)
_local = threading.local()

def conectar() -> sqlite3.Connection:
    if not getattr(_local, 'conn', None):
        conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        conn.row_factory = sqlite3.Row          # acesso por nome: row['nome']
        conn.execute("PRAGMA foreign_keys = ON;")
        conn.execute("PRAGMA journal_mode = WAL;")
        conn.execute("PRAGMA synchronous = NORMAL;")
        conn.execute("PRAGMA cache_size = -8000;")
        _local.conn = conn
    return _local.conn

def fechar_conexao():
    conn = getattr(_local, 'conn', None)
    if conn:
        conn.close()
        _local.conn = None

def inicializar_banco():
    if not os.path.exists(DB_PATH):
        print("📦 Banco de dados não encontrado. Criando estrutura...")
        conn = conectar()
        with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
            conn.executescript(f.read())
        conn.commit()
        print("✅ Banco criado com sucesso!")