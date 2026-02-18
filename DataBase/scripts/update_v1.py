from DataBase.databaseConfig import cursor, conn

#Atualizar alturas 
cursor.execute("""
UPDATE Personagens
SET AlturaClassico = 1.45,
    AlturaShippuden = 1.66
WHERE Nome = 'Naruto';
""")

cursor.execute("""
UPDATE Personagens
SET AlturaClassico = 1.50,
    AlturaShippuden = 1.68
WHERE Nome = 'Sasuke'
""")

cursor.execute("""
UPDATE Personagens
SET AlturaClassico = 1.48,
    AlturaShippuden = 1.61
WHERE Nome = 'Sakura'
""")

cursor.execute("""
UPDATE Personagens
SET AlturaClassico = 1.81,
    AlturaShippuden = 1.81
WHERE Nome = 'Kakashi'
""")

#Remover rank do Sharingan
cursor.execute("""
UPDATE Jutsus
SET Rank = NULL
WHERE Nome = 'Sharingan'
""")

conn.commit()