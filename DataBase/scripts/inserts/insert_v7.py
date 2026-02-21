from DataBase.databaseConfig import cursor, conn

cursor.execute('''
INSERT INTO Grupos (Nome, Descricao, Tipo) VALUES               

-- TIMES
('Time 7',
 'Equipe formada por Naruto Uzumaki, Sasuke Uchiha e Sakura Haruno, liderados por Kakashi Hatake.',
 'Time'),

('Time 8',
 'Equipe composta por Kiba Inuzuka, Hinata Hyuga e Shino Aburame, liderados por Kurenai Yuhi.',
 'Time'),

('Time 10',
 'Equipe formada por Shikamaru Nara, Ino Yamanaka e Choji Akimichi, liderados por Asuma Sarutobi.',
 'Time'),

('Time Guy',
 'Equipe composta por Neji Hyuga, Rock Lee e Tenten, liderados por Might Guy.',
 'Time'),

-- ORGANIZACOES CRIMINOSAS
('Akatsuki',
 'Organizacao criminosa composta por ninjas renegados de alto nivel, liderada inicialmente por Pain.',
 'Organizacao'),

('Quarteto do Som',
 'Grupo de ninjas subordinados a Orochimaru, especializados em selos amaldiçoados.',
 'Organizacao'),

-- ORGANIZACOES / DIVISOES
('ANBU',
 'Forca especial de operacoes secretas da Vila da Folha.',
 'Divisao'),

('Raiz',
 'Divisao secreta da ANBU liderada por Danzo Shimura.',
 'Divisao'),
               
('Sete Espadachins da Névoa',
 'Grupo de elite da Vila da Névoa composto por espadachins lendarios que empunham espadas especiais unicas.',
 'Organizacao'),
        
 (
    'Sannin Lendarios',
    'Time lendario formado por Jiraiya, Tsunade e Orochimaru, discipulos do Terceiro Hokage.',
    'Time'
);
''')

cursor.execute('''
INSERT INTO PersonagensGrupos (IdPersonagem, IdGrupo, Papel)

-- TIME 7
SELECT p.IdPersonagem, g.IdGrupo, 'Membro'
FROM Personagens p, Grupos g
WHERE p.Nome = 'Naruto' AND g.Nome = 'Time 7'

UNION ALL
SELECT p.IdPersonagem, g.IdGrupo, 'Membro'
FROM Personagens p, Grupos g
WHERE p.Nome = 'Sasuke' AND g.Nome = 'Time 7'

UNION ALL
SELECT p.IdPersonagem, g.IdGrupo, 'Membro'
FROM Personagens p, Grupos g
WHERE p.Nome = 'Sakura' AND g.Nome = 'Time 7'

UNION ALL
SELECT p.IdPersonagem, g.IdGrupo, 'Lider'
FROM Personagens p, Grupos g
WHERE p.Nome = 'Kakashi' AND g.Nome = 'Time 7'


-- TIME 8

UNION ALL
SELECT p.IdPersonagem, g.IdGrupo, 'Lider'
FROM Personagens p, Grupos g
WHERE p.Nome = 'Kurenai' AND g.Nome = 'Time 8'

UNION ALL
SELECT p.IdPersonagem, g.IdGrupo, 'Membro'
FROM Personagens p, Grupos g
WHERE p.Nome = 'Kiba' AND g.Nome = 'Time 8'

UNION ALL
SELECT p.IdPersonagem, g.IdGrupo, 'Membro'
FROM Personagens p, Grupos g
WHERE p.Nome = 'Hinata' AND g.Nome = 'Time 8'

UNION ALL
SELECT p.IdPersonagem, g.IdGrupo, 'Membro'
FROM Personagens p, Grupos g
WHERE p.Nome = 'Shino' AND g.Nome = 'Time 8'


-- TIME 10

UNION ALL
SELECT p.IdPersonagem, g.IdGrupo, 'Lider'
FROM Personagens p, Grupos g
WHERE p.Nome = 'Asuma' AND g.Nome = 'Time 10'

UNION ALL
SELECT p.IdPersonagem, g.IdGrupo, 'Membro'
FROM Personagens p, Grupos g
WHERE p.Nome = 'Shikamaru' AND g.Nome = 'Time 10'

UNION ALL
SELECT p.IdPersonagem, g.IdGrupo, 'Membro'
FROM Personagens p, Grupos g
WHERE p.Nome = 'Ino' AND g.Nome = 'Time 10'

UNION ALL
SELECT p.IdPersonagem, g.IdGrupo, 'Membro'
FROM Personagens p, Grupos g
WHERE p.Nome = 'Choji' AND g.Nome = 'Time 10'

-- TIME GUY
       
UNION ALL
SELECT p.IdPersonagem, g.IdGrupo, 'Lider'
FROM Personagens p, Grupos g
WHERE p.Nome = 'Might' AND g.Nome = 'Time Guy'

UNION ALL
SELECT p.IdPersonagem, g.IdGrupo, 'Membro'
FROM Personagens p, Grupos g
WHERE p.Nome = 'Rock' AND g.Nome = 'Time Guy'

UNION ALL
SELECT p.IdPersonagem, g.IdGrupo, 'Membro'
FROM Personagens p, Grupos g
WHERE p.Nome = 'Neji' AND g.Nome = 'Time Guy'

UNION ALL
SELECT p.IdPersonagem, g.IdGrupo, 'Membro'
FROM Personagens p, Grupos g
WHERE p.Nome = 'Tenten' AND g.Nome = 'Time Guy'


-- AKATSUKI
       
UNION ALL
SELECT p.IdPersonagem, g.IdGrupo, 'Membro'
FROM Personagens p, Grupos g
WHERE p.Nome = 'Itachi' AND g.Nome = 'Akatsuki'

UNION ALL
SELECT p.IdPersonagem, g.IdGrupo, 'Membro'
FROM Personagens p, Grupos g
WHERE p.Nome = 'Kisame' AND g.Nome = 'Akatsuki'



-- QUARTETO DO SOM

UNION ALL
SELECT p.IdPersonagem, g.IdGrupo, 'Lider'
FROM Personagens p, Grupos g
WHERE p.Nome = 'Orochimaru' AND g.Nome = 'Quarteto do Som'

UNION ALL
SELECT p.IdPersonagem, g.IdGrupo, 'Membro'
FROM Personagens p, Grupos g
WHERE p.Nome = 'Tayuya' AND g.Nome = 'Quarteto do Som'

UNION ALL
SELECT p.IdPersonagem, g.IdGrupo, 'Membro'
FROM Personagens p, Grupos g
WHERE p.Nome = 'Sakon/Ukon' AND g.Nome = 'Quarteto do Som'

UNION ALL
SELECT p.IdPersonagem, g.IdGrupo, 'Membro'
FROM Personagens p, Grupos g
WHERE p.Nome = 'Jirobo' AND g.Nome = 'Quarteto do Som'

UNION ALL
SELECT p.IdPersonagem, g.IdGrupo, 'Membro'
FROM Personagens p, Grupos g
WHERE p.Nome = 'Kidomaru' AND g.Nome = 'Quarteto do Som'
;
''')

conn.commit()