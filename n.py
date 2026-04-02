import sqlite3

doc = sqlite3.connect('banco.db')
cs = doc.cursor()

cs.execute('''
        CREATE TABLE IF NOT EXISTS dados(
        nome TEXT,
        idade INTEGER,
        email TEXT,   
        endereço TEXT,
        trabalho TEXT,
        graduação  TEXT''' )

nome = input('nome:')
idade = int(input('idade:'))
email = input('email:')
trabalho = input('trabalho:')
graduação = input('graduação:')


cs.execute(('INSERT INTO dados VALUE:(?,?,?,?,?)'), (nome,idade,email,trabalho,graduação))

doc.commit()