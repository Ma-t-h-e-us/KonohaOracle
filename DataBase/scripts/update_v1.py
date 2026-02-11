from DataBase.databaseConfig import cursor, conn

#Permitir NULL no Rank
cursor.execute("""
ALTER TABLE Jutsus
MODIFY Rank VARCHAR(2) NULL
""")

#Atualizar alturas (Shippuden)

cursor.execute("""
UPDATE Personagens
SET Altura = 1.66
WHERE Nome = 'Naruto Uzumaki'
""")

cursor.execute("""
UPDATE Personagens
SET Altura = 1.68
WHERE Nome = 'Sasuke Uchiha'
""")

cursor.execute("""
UPDATE Personagens
SET Altura = 1.61
WHERE Nome = 'Sakura Haruno'
""")

cursor.execute("""
UPDATE Personagens
SET Altura = 1.81
WHERE Nome = 'Kakashi Hatake'
""")

#Remover rank do Sharingan
cursor.execute("""
UPDATE Jutsus
SET Rank = NULL
WHERE Nome = 'Sharingan'
""")

conn.commit()