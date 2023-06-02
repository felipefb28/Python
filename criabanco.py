import sqlite3

con=sqlite3.connect('clientes.db')

#Definindo um cursos
cursor=con.cursor()
cursor.execute("""

            CREATE TABLE clientes (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER,
                cpf     VARCHAR(11) NOT NULL,
                email TEXT NOT NULL,
                fone TEXT,
                cidade TEXT,
                uf VARCHAR(2) NOT NULL,
                criado_em DATE NOT NULL
            );""")
print('tabela criada com sucesso')
