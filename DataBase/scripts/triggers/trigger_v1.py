from DataBase.databaseConfig import cursor, conn

cursor.execute('''
CREATE OR REPLACE FUNCTION adicionar_jutsus_basicos()
RETURNS TRIGGER AS $$
BEGIN

    IF EXISTS (
        SELECT 1 FROM Ocupacoes
        WHERE IdOcupacao IN (NEW.IdOcupacaoClassico, NEW.IdOcupacaoShippuden)
        AND Nome IN ('Genin','Chunin','Jounin','Nukenin','Hokage','Kazekage','Mizukage','Raikage','Tsuchikage')
    )
    THEN

        INSERT INTO PersonagensJutsus (IdPersonagem, IdJutsu)
        SELECT NEW.IdPersonagem, IdJutsu
        FROM Jutsus
        WHERE Nome IN (
            'Clonagem',
            'Transformacao',
            'Tecnica de Substituicao'
        )
        ON CONFLICT DO NOTHING;

    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
''')

cursor.execute('''
DROP TRIGGER IF EXISTS trigger_jutsus_basicos ON Personagens;
''')

cursor.execute('''
CREATE TRIGGER trigger_jutsus_basicos
AFTER INSERT ON Personagens
FOR EACH ROW
EXECUTE FUNCTION adicionar_jutsus_basicos();
''')

conn.commit()