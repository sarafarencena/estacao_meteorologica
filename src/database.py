import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'dados.db')
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), 'schema.sql')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH, timeout=10)
    conn.execute('PRAGMA journal_mode=WAL')
    conn.execute('PRAGMA busy_timeout=5000')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    with open(SCHEMA_PATH, 'r') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

def inserir_leitura(temperatura, umidade, pressao=None):
    conn = get_db_connection()
    cursor = conn.execute(
        'INSERT INTO leituras (temperatura, umidade, pressao) VALUES (?, ?, ?)',
        (temperatura, umidade, pressao)
    )
    conn.commit()
    id_novo = cursor.lastrowid
    conn.close()
    return id_novo

def listar_leituras(limite=50):
    conn = get_db_connection()
    rows = conn.execute(
        'SELECT * FROM leituras ORDER BY timestamp DESC LIMIT ?',
        (limite,)
    ).fetchall()
    conn.close()
    return rows

def buscar_leitura(id):
    conn = get_db_connection()
    row = conn.execute(
        'SELECT * FROM leituras WHERE id = ?', (id,)
    ).fetchone()
    conn.close()
    return row

def atualizar_leitura(id, dados):
    conn = get_db_connection()
    conn.execute(
        'UPDATE leituras SET temperatura = ?, umidade = ?, pressao = ? WHERE id = ?',
        (dados['temperatura'], dados['umidade'], dados.get('pressao'), id)
    )
    conn.commit()
    conn.close()

def deletar_leitura(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM leituras WHERE id = ?', (id,))
    conn.commit()
    conn.close()

def estatisticas():
    conn = get_db_connection()
    row = conn.execute('''
        SELECT
            AVG(temperatura) as temp_media,
            MIN(temperatura) as temp_min,
            MAX(temperatura) as temp_max,
            AVG(umidade)     as umid_media,
            MIN(umidade)     as umid_min,
            MAX(umidade)     as umid_max
        FROM leituras
    ''').fetchone()
    conn.close()
    return row