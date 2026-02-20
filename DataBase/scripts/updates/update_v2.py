from DataBase.databaseConfig import cursor, conn

cursor.execute("""
DROP TRIGGER IF EXISTS trigger_jutsus_basicos ON Personagens;
""")

cursor.execute("""
DROP FUNCTION IF EXISTS adicionar_jutsus_basicos();
""") 

conn.commit()