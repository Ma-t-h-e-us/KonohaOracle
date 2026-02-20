from DataBase.databaseConfig import cursor, conn

cursor.execute('''
INSERT INTO PersonagensHabilidades (IdPersonagem, IdHabilidade)
VALUES

-- NARUTO
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Naruto'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Vigor Fisico Elevado')),

((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Naruto'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Jinchuuriki')),

-- SASUKE
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Sasuke'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Sharingan')),

((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Sasuke'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Combate a Longa Distancia')),
               
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Sasuke'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Marca da Maldicao')),

-- SAKURA

((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Sakura'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Ninjutsu Medico')),

-- SHIKAMARU
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Shikamaru'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Estrategista')),

((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Shikamaru'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Lideranca')),

-- NEJI
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Neji'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Byakugan')),

((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Neji'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Mestre em Taijutsu')),

((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Neji'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Rastreamento Avancado')),

-- KIBA
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Kiba'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Olfato Agucado')),

((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Kiba'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Rastreamento Avancado')),

-- SHINO
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Shino'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Rastreamento Avancado')),

((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Shino'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Combate a Longa Distancia')),

-- ROCK LEE
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Rock'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Mestre em Taijutsu')),

((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Rock'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Velocidade Elevada')),

((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Rock'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Vigor Fisico Elevado')),

-- HINATA
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Hinata'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Byakugan')),

((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Hinata'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Mestre em Taijutsu')),

-- OROCHIMARU
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Orochimaru'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Imortalidade')),

((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Orochimaru'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Manipulacao Psicologica')),

((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Orochimaru'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Criador de Jutsus')),

((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Orochimaru'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Mestre em Kenjutsu')),

-- KAKASHI
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Kakashi'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Sharingan')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Kakashi'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Experiencia em Combate')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Kakashi'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Combate a Longa Distancia')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Kakashi'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Mestre em Taijutsu')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Kakashi'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Lideranca')),

-- JIRAIYA
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Jiraiya'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Modo Sabio')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Jiraiya'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Experiencia em Combate')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Jiraiya'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Mestre em Taijutsu')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Jiraiya'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Criador de Jutsus')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Jiraiya'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Espionagem')),

-- TSUNADE
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Tsunade'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Ninjutsu Medico')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Tsunade'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Regeneracao Acelerada')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Tsunade'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Forca Elevada')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Tsunade'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Lideranca')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Tsunade'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Experiencia em Combate')),

-- ASUMA
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Asuma'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Combate a Longa Distancia')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Asuma'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Experiencia em Combate')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Asuma'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Lideranca')),

-- KURENAI
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Kurenai'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Especialista em Genjutsu')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Kurenai'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Experiencia em Combate')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Kurenai'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Lideranca')),

-- ITACHI
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Itachi'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Sharingan')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Itachi'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Especialista em Genjutsu')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Itachi'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Manipulacao Psicologica')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Itachi'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Estrategista')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Itachi'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Combate a Longa Distancia')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Itachi'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Experiencia em Combate')),

-- KISAME
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Kisame'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Combate a Longa Distancia')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Kisame'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Vigor Fisico Elevado')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Kisame'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Experiencia em Combate')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Kisame'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Mestre em Kenjutsu')),

-- HIRUZEN
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Hiruzen'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Experiencia em Combate')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Hiruzen'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Estrategista')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Hiruzen'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Combate a Longa Distancia')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Hiruzen'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Lideranca')),

-- KABUTO
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Kabuto'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Ninjutsu Medico')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Kabuto'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Manipulacao Psicologica')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Kabuto'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Experiencia em Combate')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Kabuto'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Espionagem')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Kabuto'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Controle de Chakra')),

-- ZABUZA
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Zabuza'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Mestre em Kenjutsu')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Zabuza'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Combate a Longa Distancia')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Zabuza'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Experiencia em Combate')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Zabuza'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Vigor Fisico Elevado')),

-- HAKU
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Haku'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Combate a Longa Distancia')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Haku'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Ninja Sensorial')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Haku'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Velocidade Elevada')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Haku'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Experiencia em Combate')),

-- KIDOMARU
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Kidomaru'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Combate a Longa Distancia')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Kidomaru'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Marca da Maldicao')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Kidomaru'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Experiencia em Combate')),

-- TAYUYA
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Tayuya'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Especialista em Genjutsu')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Tayuya'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Combate a Longa Distancia')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Tayuya'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Marca da Maldicao')),

-- Sakon/Ukon
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Sakon/Ukon'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Mestre em Taijutsu')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Sakon/Ukon'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Marca da Maldicao')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Sakon/Ukon'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Vigor Fisico Elevado')),

-- JIROBO
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Jirobo'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Forca Elevada')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Jirobo'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Vigor Fisico Elevado')),
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Jirobo'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Marca da Maldicao')),          

-- KIMIMARO
((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Kimimaro'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Mestre em Taijutsu')),

((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Kimimaro'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Experiencia em Combate')),

((SELECT IdPersonagem FROM Personagens WHERE Nome = 'Kimimaro'),
 (SELECT IdHabilidade FROM Habilidades WHERE Nome = 'Marca da Maldicao'));
''')

conn.commit()