from DataBase.databaseConfig import cursor, conn

#jutsus básicos
cursor.execute('''
INSERT INTO Jutsus (IdElemento, IdTipoJutsu, Nome, Descricao, Rank)
VALUES

(
    (SELECT IdElemento FROM Elementos WHERE Nome = 'Nenhum'),
    (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome = 'Ninjutsu'),
    'Clonagem',
    'Cria clones ilusorios sem massa fisica para confundir o inimigo.',
    'D'
),

(
    (SELECT IdElemento FROM Elementos WHERE Nome = 'Nenhum'),
    (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome = 'Ninjutsu'),
    'Transformacao',
    'Permite ao usuario assumir a forma de outra pessoa ou objeto.',
    'D'
),

(
    (SELECT IdElemento FROM Elementos WHERE Nome = 'Nenhum'),
    (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome = 'Ninjutsu'),
    'Tecnica de Substituicao',
    'Permite trocar de lugar rapidamente com um objeto para evitar um ataque.',
    'D'
);
''')


cursor.execute('''
INSERT INTO PersonagensJutsus (IdPersonagem, IdJutsu)
SELECT p.IdPersonagem, j.IdJutsu
FROM Personagens p
CROSS JOIN Jutsus j
WHERE j.Nome IN (
    'Clonagem',
    'Transformacao',
    'Tecnica de Substituicao'
)
AND (
    p.IdOcupacaoClassico IN (
        SELECT IdOcupacao FROM Ocupacoes
        WHERE Nome IN ('Genin','Chunin','Jounin','Nukenin','Hokage','Kazekage','Mizukage','Raikage','Tsuchikage')
    )
    OR
    p.IdOcupacaoShippuden IN (
        SELECT IdOcupacao FROM Ocupacoes
        WHERE Nome IN ('Genin','Chunin','Jounin','Nukenin','Hokage','Kazekage','Mizukage','Raikage','Tsuchikage')
    )
)
ON CONFLICT DO NOTHING;
''')

cursor.execute('''
INSERT INTO Jutsus (IdElemento, IdTipoJutsu, Nome, Descricao, Rank)
VALUES

-- Taijutsu (Guy / Lee / Neji)
((SELECT IdElemento FROM Elementos WHERE Nome='Nenhum'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Taijutsu'),
 'Lotus Primaria',
 'Golpe devastador usando abertura do Primeiro Portao.',
 'B'),

((SELECT IdElemento FROM Elementos WHERE Nome='Nenhum'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Taijutsu'),
 'Sombra da Folha Dancante',
 'Chute ascendente que lança o inimigo ao ar.',
 'C'),

((SELECT IdElemento FROM Elementos WHERE Nome='Nenhum'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Taijutsu'),
 'Palma Aerea',
 'Golpe de ar comprimido com chakra.',
 NULL),

((SELECT IdElemento FROM Elementos WHERE Nome='Nenhum'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Taijutsu'),
 'Oito Trigramas: Sessenta e Quatro Golpes',
 'Sequencia de ataques que bloqueiam o fluxo de chakra.',
 NULL),

((SELECT IdElemento FROM Elementos WHERE Nome='Nenhum'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Taijutsu'),
 'Oito Trigramas: Rotacao',
 'Defesa absoluta baseada no giro de chakra.',
 NULL),

((SELECT IdElemento FROM Elementos WHERE Nome='Nenhum'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Taijutsu'),
 'Entrada Dinamica',
 'Investida veloz com chute explosivo.',
 'D'),

((SELECT IdElemento FROM Elementos WHERE Nome='Nenhum'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Taijutsu'),
 'Pavao do Amanhecer',
 'Ataque em alta velocidade com chamas criadas pelo atrito.',
 'A'),

((SELECT IdElemento FROM Elementos WHERE Nome='Nenhum'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Taijutsu'),
 'Hirudora',
 'Tigre de ar comprimido gerado pelo Setimo Portao.',
 'A'),

((SELECT IdElemento FROM Elementos WHERE Nome='Nenhum'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Taijutsu'),
 'Yagai',
 'Golpe final do Oitavo Portao da Morte.',
 'S'),

-- Agua
((SELECT IdElemento FROM Elementos WHERE Nome='Agua'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Ninjutsu'),
 'Parede de Agua',
 'Barreira defensiva de agua.',
 'B'),

((SELECT IdElemento FROM Elementos WHERE Nome='Agua'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Ninjutsu'),
 'Bomba do Tubarao de Agua',
 'Projeta um tubarao de agua contra o inimigo.',
 'B'),

((SELECT IdElemento FROM Elementos WHERE Nome='Agua'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Ninjutsu'),
 'Cinco Tubaroes Famintos',
 'Invoca cinco tubaroes de agua para atacar.',
 'B'),

((SELECT IdElemento FROM Elementos WHERE Nome='Agua'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Ninjutsu'),
 'Tecnica da Grande Bomba do Tubarao',
 'Gigantesco tubarao de agua que absorve chakra.',
 'A'),

((SELECT IdElemento FROM Elementos WHERE Nome='Agua'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Ninjutsu'),
 'Prisao de Agua',
 'Aprisiona o inimigo em uma esfera de agua.',
 'C'),

((SELECT IdElemento FROM Elementos WHERE Nome='Agua'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Ninjutsu'),
 'Clone de Agua',
 'Cria clone feito de agua.',
 'C'),

-- Terra
((SELECT IdElemento FROM Elementos WHERE Nome='Terra'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Ninjutsu'),
 'Parede de Lama',
 'Barreira defensiva de terra.',
 'B'),

-- Fogo
((SELECT IdElemento FROM Elementos WHERE Nome='Fogo'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Ninjutsu'),
 'Amaterasu',
 'Chamas negras eternas do Mangekyo Sharingan.',
 NULL),

((SELECT IdElemento FROM Elementos WHERE Nome='Fogo'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Ninjutsu'),
 'Cinzas Ardentes',
 'Nuvem de cinzas explosivas.',
 'B'),

((SELECT IdElemento FROM Elementos WHERE Nome='Fogo'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Ninjutsu'),
 'Bomba do Dragao Flamejante',
 'Dragao de fogo concentrado.',
 'B'),

-- Gelo (Kekkei Genkai)
((SELECT IdElemento FROM Elementos WHERE Nome='Gelo'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Ninjutsu'),
 'Espelhos Demoniacos de Cristais de Gelo',
 'Cria espelhos de gelo para ataques em alta velocidade.',
 NULL),

((SELECT IdElemento FROM Elementos WHERE Nome='Gelo'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Ninjutsu'),
 'Mil Agulhas Voadoras de Agua da Morte',
 'Projeta agulhas de gelo em alta velocidade.',
 NULL),

-- Som
((SELECT IdElemento FROM Elementos WHERE Nome='Nenhum'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Genjutsu'),
 'Flauta Demoníaca: Correntes Ilusorias de Som',
 'Genjutsu sonoro que paralisa o alvo.',
 'B'),

((SELECT IdElemento FROM Elementos WHERE Nome='Nenhum'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Ninjutsu'),
 'Flauta Demoníaca: Manipulacao dos Guerreiros Fantasmas',
 'Invoca criaturas demoníacas controladas por som.',
 'B'),

-- Sombras
((SELECT IdElemento FROM Elementos WHERE Nome='Nenhum'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Ninjutsu'),
 'Possessao das Sombras',
 'Estende a sombra para controlar o oponente.',
 NULL),

-- Yamanaka
((SELECT IdElemento FROM Elementos WHERE Nome='Nenhum'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Ninjutsu'),
 'Transferencia de Mente',
 'Transfere a consciencia para o corpo do inimigo.',
 'C'),

-- Uchiha
((SELECT IdElemento FROM Elementos WHERE Nome='Nenhum'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Genjutsu'),
 'Tsukuyomi',
 'Genjutsu supremo do Mangekyo Sharingan, o reino dos pesadelos.',
 NULL),

-- Akimichi
((SELECT IdElemento FROM Elementos WHERE Nome='Nenhum'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Ninjutsu'),
 'Expansao Humana',
 'Aumenta o tamanho do corpo.',
 'C'),

-- Inuzuka
((SELECT IdElemento FROM Elementos WHERE Nome='Nenhum'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Ninjutsu'),
 'Mimetismo da Besta',
 'Assume caracteristicas de animal.',
 'C'),

((SELECT IdElemento FROM Elementos WHERE Nome='Nenhum'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Taijutsu'),
 'Presa sobre Presa',
 'Ataque giratorio combinado com parceiro canino.',
 'B'),

((SELECT IdElemento FROM Elementos WHERE Nome='Nenhum'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Ninjutsu'),
 'Lobo de Tres Cabecas',
 'Transformacao conjunta em lobo gigante.',
 NULL),

-- Kidomaru
((SELECT IdElemento FROM Elementos WHERE Nome='Nenhum'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Ninjutsu'),
 'Arco da Aranha',
 'Arma feita de teia endurecida.',
 NULL),

-- Sakon/Ukon
((SELECT IdElemento FROM Elementos WHERE Nome='Nenhum'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Ninjutsu'),
 'Tecnica da Destruicao Parasita Demoniaca',
 'Funde-se ao corpo do inimigo para destruicao interna.',
 NULL),

-- Barreira
((SELECT IdElemento FROM Elementos WHERE Nome='Nenhum'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Fuuinjutsu'),
 'Formacao das Quatro Chamas Purpuras',
 'Barreira de selamento usada pelos quatro do som.',
 'A'),

-- Selo
((SELECT IdElemento FROM Elementos WHERE Nome='Nenhum'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Fuuinjutsu'),
 'Selo do Ceifeiro da Morte',
 'Invoca o Shinigami para selar almas.',
 'S'),

-- Armas
((SELECT IdElemento FROM Elementos WHERE Nome='Nenhum'),
 (SELECT IdTipoJutsu FROM TiposJutsu WHERE Nome='Ninjutsu'),
 'Clone da Sombra de Shuriken',
 'Multiplica shurikens durante o lancamento.',
 'A');
''')

cursor.execute('''
INSERT INTO PersonagensJutsus (IdPersonagem, IdJutsu)
SELECT p.IdPersonagem, j.IdJutsu
FROM Personagens p
JOIN Jutsus j ON TRUE
WHERE

(
    (p.Nome='Might' AND p.Sobrenome='Guy') AND
    j.Nome IN ('Entrada Dinamica','Pavao do Amanhecer','Hirudora','Yagai')
)

OR

-- ROCK LEE
(
    (p.Nome='Rock' AND p.Sobrenome='Lee') AND
    j.Nome IN ('Lotus Primaria','Sombra da Folha Dancante')
)

OR

-- NEJI
(
    (p.Nome='Neji') AND
    j.Nome IN (
        'Palma Aerea',
        'Oito Trigramas: Sessenta e Quatro Golpes',
        'Oito Trigramas: Rotacao'
    )
)

OR

-- HINATA
(
    (p.Nome='Hinata') AND
    j.Nome IN (
        'Palma Aerea',
        'Oito Trigramas: Sessenta e Quatro Golpes'
    )
)

OR

-- KIBA
(
    (p.Nome='Kiba') AND
    j.Nome IN (
        'Mimetismo da Besta',
        'Presa sobre Presa',
        'Lobo de Tres Cabecas'
    )
)

OR

-- SHIKAMARU
(
    (p.Nome='Shikamaru') AND
    j.Nome='Possessao das Sombras'
)

OR

-- INO
(
    (p.Nome='Ino') AND
    j.Nome='Transferencia de Mente'
)

OR

-- CHOJI
(
    (p.Nome='Choji') AND
    j.Nome='Expansao Humana'
)

OR

-- ASUMA
(
    (p.Nome='Asuma') AND
    j.Nome IN ('Cinzas Ardentes','Lamina de Chakra')
)

OR

-- KAKASHI
(
    (p.Nome='Kakashi') AND
    j.Nome IN (
        'Parede de Agua',
        'Bomba do Tubarao de Agua',
        'Clone de Agua',
        'Prisao de Agua'
    )
)

OR

-- ZABUZA
(
    (p.Nome='Zabuza') AND
    j.Nome IN (
        'Prisao de Agua',
        'Parede de Agua'
    )
)

OR

-- HAKU
(
    (p.Nome='Haku') AND
    j.Nome IN (
        'Espelhos Demoniacos de Cristais de Gelo',
        'Mil Agulhas Voadoras de Agua da Morte'
    )
)

OR

-- ITACHI
(
    (p.Nome='Itachi') AND
    j.Nome IN ('Amaterasu','Tsukuyomi')
)

OR

-- KISAME
(
    (p.Nome='Kisame') AND
    j.Nome IN (
        'Bomba do Tubarao de Agua',
        'Cinco Tubaroes Famintos',
        'Tecnica da Grande Bomba do Tubarao'
    )
)

OR

-- TAYUYA
(
    (p.Nome='Tayuya') AND
    j.Nome IN (
        'Flauta Demoníaca: Correntes Ilusorias de Som',
        'Flauta Demoníaca: Manipulacao dos Guerreiros Fantasmas',
        'Formacao das Quatro Chamas Purpuras'
    )
)

OR

-- SAKON/UKON
(
    (p.Nome='Sakon/Ukon') AND
    j.Nome IN (
        'Tecnica da Destruicao Parasita Demoniaca',
        'Formacao das Quatro Chamas Purpuras'
    )
)

OR

-- JIROBO
(
    (p.Nome='Jirobo') AND
    j.Nome IN (
        'Parede de Lama',
        'Formacao das Quatro Chamas Purpuras'
    )
)

OR

-- KIDOMARU
(
    (p.Nome='Kidomaru') AND
    j.Nome IN ('Arco da Aranha','Formacao das Quatro Chamas Purpuras')
)

ON CONFLICT DO NOTHING;
''')

conn.commit()