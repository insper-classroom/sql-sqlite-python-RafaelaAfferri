import sqlite3


def criar_tabelas(nome,caminho, coluna ):
    conn = sqlite3.connect(caminho)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS {nome} (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            {coluna[1]} TEXT NOT NULL,
            {coluna[2]} TEXT NOT NULL,
            {coluna[3]} INTEGER
        );
        """)
    conn.commit

def inserir_info(lista_infos, caminho, tabela):
    conn = sqlite3.connect(caminho)
    cursor = conn.cursor()


    esutdantes = lista_infos
    cursor.executemany("""
    INSERT INTO {tabela} (Nome, Curso, Ano_de_Ingresso)
    VALUES (?, ?, ?);
    """, esutdantes)

    conn.commit()

def consultar(tabela, caminho):
    conn = sqlite3.connect(caminho)
    cursor = conn.cursor()


    cursor.execute("SELECT * FROM {tabela}")
    print(cursor.fetchall())

def atualizar(tabela, caminho, objeto, tipo_atulizção, novo):
    conn = sqlite3.connect(caminho)
    cursor = conn.cursor()

    cursor.execute("UPDATE {tabela} SET {tipo_atulizção} = ? WHERE Nome = ?", (novo, objeto[0]))
    conn.commit()

def deletar(caminho, tabela, id):
    conn = sqlite3.connect(caminho)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM {Tabela} WHERE ID = ?", ({id},))
    conn.commit()
    