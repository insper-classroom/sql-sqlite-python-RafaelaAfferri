import sqlite3
from db.db_utils import *

caminho = 'db/database_alunos.db'
tabela = 'Estudantes'
coluna = ['Nome', 'Curso', 'Ano_de_Ingresso']

criar_tabelas(tabela, caminho, coluna)

lista_infos = [
            ('Ana Silva', 'Computação', 2019), 
            ('Pedro Mendes', 'Física',2021),
            ('Carla Souza', 'Computação',2020),
            ('João Alves', 'Matemática', 2018),
            ('Maria Oliveira', 'Química',  2022)
            ]


inserir_info(lista_infos, caminho, tabela)

consultar(tabela, caminho)

atualizar(tabela, caminho, ('Ana Silva', 'Computação', 2019), 'Curso', 'Física')

consultar(tabela, caminho)

deletar(caminho, tabela, 1)

consultar(tabela, caminho)



