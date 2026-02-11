from ..databaseConfig import cursor, conn

cursor.execute("""
INSERT INTO TipoPersonagens (Relevancia) VALUES
('Protagonista'),
('Deutragonista'),
('Antagonista'),
('Principais'),
('Secundarios'),
('Terciario')
""")

cursor.execute("""
INSERT INTO Clas (Nome, Descricao) VALUES
('Uzumaki', 'Clã conhecido por sua enorme vitalidade, grande reserva de chakra e domínio avançado de técnicas de selamento.'),
('Hatake', 'Clã respeitado de Konoha, famoso por ninjas habilidosos e estrategistas, como o lendário Kakashi.'),
('Uchiha', 'Clã poderoso descendente de Indra, portador do Sharingan e conhecido por seu talento excepcional em combate.'),
('Haruno', 'Clã de origem civil em Konoha, representado por membros de grande inteligência e controle preciso de chakra.')
""")

cursor.execute("""
INSERT INTO Arcos (Nome, Descricao) VALUES
('Prologo', 'Introdução da história de Naruto, apresentando o Time 7 e a vida inicial na Vila da Folha.'),
('Pais das Ondas', 'Primeira missão real do Time 7, enfrentando Zabuza e Haku em defesa de Tazuna.'),
('Exame Chunin', 'Competição entre vilas para promoção de ninjas, marcada por lutas intensas e invasão surpresa.'),
('Ataque a Vila da Folha', 'Invasão liderada por Orochimaru durante o Exame Chunin, resultando na morte do Terceiro Hokage.'),
('Busca por Tsunade', 'Naruto e Jiraiya procuram Tsunade para assumir o posto de Quinta Hokage.'),
('Missao de Recuperacao de Sasuke', 'Equipe formada para impedir que Sasuke abandone Konoha e se una a Orochimaru.')
""")

cursor.execute("""
INSERT INTO Vilas (Nome, Pais) VALUES
('Vila Oculta da Folha', 'Fogo'),
('Vila Oculta da Areia', 'Vento'),
('Vila Oculta da Nevoa', 'Agua'),
('Vila Oculta da Nuvem', 'Relampago'),
('Vila Oculta da Pedra', 'Terra')
""")

cursor.execute("""
INSERT INTO Ocupacoes (Nome) VALUES
('Genin'),
('Chunin'),
('Jounin'),
('Jounin especial'),
('Hokage'),
('Kazekage'),
('Mizukage'),
('Raikage'),
('Tsuchikage'),
('Civil'),
('Animal')
""")

cursor.execute("""
INSERT INTO TiposElementos (Nome) VALUES
('Elemento Basico'),
('Kekkei Genkai'),
('Kekkei Touta')
""")

cursor.execute("""
INSERT INTO TiposJutsu (Nome) VALUES
('Taijutsu'),
('Genjutsu'),
('Ninjutsu'),
('Fuuinjutsu'),
('Ninjutsu Medico'),
('Kinjutsu'),
('Nenhum')
""")

cursor.execute("""
INSERT INTO Elementos (IdTiposElementos, Nome) VALUES
-- Elementos Básicos
(1, 'Fogo'),
(1, 'Agua'),
(1, 'Terra'),
(1, 'Relampago'),
(1, 'Vento'),

-- Yin-Yang (tratado como básico especial)
(1, 'Yin-Yang'),

-- Kekkei Genkai
(2, 'Gelo'),
(2, 'Lava'),
(2, 'Vapor'),
(2, 'Explosao'),

-- Kekkei Touta
(3, 'Poeira'),

-- Outros
(1, 'Nenhum')
""")

cursor.execute("""
INSERT INTO Personagens (
    IdTipoPersonagem, IdCla, IdArcoAparicao,
    IdOcupacaoClassico, IdOcupacaoShippuden,
    IdVila, Nome, Idade_Clasico, Idade_Shippuden,
    Sexo, DataNascimento, Altura,
    CorCabelo, CorOlhos, CorPele,
    MissoesCompletas, Descricao, Estado
) VALUES

-- Naruto
(1, 1, 1,
1, 1,
1, 'Naruto Uzumaki', 12, 15,
'Masculino', '1987-10-10', 145.00,
'Loiro', 'Azul', 'Clara',
7,
'Ninja impulsivo do Time 7 que sonha em se tornar Hokage para ser reconhecido por todos. Determinado e leal, nunca desiste de seus amigos.',
'Vivo'),

-- Sasuke
(2, 3, 1,
1, 1,
1, 'Sasuke Uchiha', 12, 15,
'Masculino', '1988-07-23', 150.00,
'Preto', 'Preto', 'Clara',
7,
'Prodigio do clã Uchiha e membro do Time 7. Inicialmente busca vingança contra seu irmão e demonstra personalidade fria e reservada.',
'Vivo'),

-- Sakura
(4, 4, 1,
1, 1,
1, 'Sakura Haruno', 12, 15,
'Feminino', '1988-03-28', 148.00,
'Rosa', 'Verde', 'Clara',
7,
'Integrante do Time 7, destaca-se por sua inteligência e controle de chakra. Deseja evoluir como ninja e proteger seus companheiros.',
'Vivo'),

-- Kakashi
(4, 2, 1,
3, 3,
1, 'Kakashi Hatake', 26, 29,
'Masculino', '1961-09-15', 181.00,
'Prata', 'Cinza', 'Clara',
1000,
'Jounin lider do Time 7, conhecido como Ninja Copiador. Calmo e estrategista, valoriza o trabalho em equipe acima das regras.',
'Vivo')
""")

cursor.execute("""
INSERT INTO Jutsus (IdElemento, IdTipoJutsu, Nome, Descricao, Rank) VALUES

-- Naruto
(12, 3, 'Clone das Sombras', 'Tecnica que cria copias fisicas reais do usuario.', 'B'),
(12, 3, 'Rasengan', 'Esfera de chakra concentrado de alto poder destrutivo.', 'A'),

-- Sasuke
(4, 3, 'Chidori', 'Tecnica de alta velocidade baseada em relampago.', 'A'),
(1, 3, 'Bola de Fogo', 'Classica tecnica Uchiha de fogo.', 'C'),
(1, 3, 'Flor de Fenix', 'Dispara multiplas pequenas bolas de fogo.', 'C'),
(12, 2, 'Sharingan', 'Doujutsu do cla Uchiha que copia tecnicas e antecipa movimentos.', 'A'),

-- Agua
(2, 3, 'Dragao de Agua', 'Cria um grande dragao feito de agua para atacar.', 'B'),
(2, 3, 'Vortex de Agua', 'Forma um turbilhao de agua que aprisiona o inimigo.', 'B'),

-- Kakashi
(3, 3, 'Cacador de Cabecas', 'Tecnica de terra que prende o oponente no solo.', 'C')
""")

cursor.execute("""
INSERT INTO PersonagensJutsus (IdPersonagem, IdJutsu) VALUES
-- Naruto
(1,1),
(1,2),

-- Sasuke
(2,3),
(2,4),
(2,5),
(2,6),

-- Kakashi
(4,3),
(4,7),
(4,8),
(4,9)
""")

cursor.execute("""
INSERT INTO PersonagensElementos (IdPersonagem, IdElemento) VALUES

-- Naruto
(1,5),

-- Sasuke
(2,1),
(2,4),

-- Kakashi (5 basicos)
(4,1),
(4,2),
(4,3),
(4,4),
(4,5)
""")

conn.commit()