#INSERCAO DE LUTAS

from DataBase.databaseConfig import cursor, conn

cursor.execute('''
INSERT INTO Confrontos (Descricao, IdArco, Local, ResultadoDescricao)
VALUES (
    'Naruto vs Neji',
    (SELECT IdArco FROM Arcos WHERE Nome = 'Exame Chunin'),
    'Arena da Vila da Folha',
    'Naruto derrota Neji usando chakra da Raposa de 9 caudas'
),
(
    'Rock Lee vs Gaara',
    (SELECT IdArco FROM Arcos WHERE Nome = 'Exame Chunin'),
    'Arena de preliminares do Exame Chunin',
    'Gaara vence após Lee abrir os Portões Internos'
),
(
    'Naruto e Sasuke vs Haku',
    (SELECT IdArco FROM Arcos WHERE Nome = 'Pais das Ondas'),
    'Ponte em construção',
    'Haku morre protegendo Zabuza'
),
(
    'Hiruzen vs Orochimaru',
    (SELECT IdArco FROM Arcos WHERE Nome = 'Ataque a Vila da Folha'),
    'Telhado do prédio do Hokage',
    'Hiruzen morre selando os braços de Orochimaru atraves do Ceifeiro da Morte'
),
(
    'Naruto vs Gaara',
    (SELECT IdArco FROM Arcos WHERE Nome = 'Ataque a Vila da Folha'),
    'Floresta da Vila da Folha',
    'Naruto vence Gaara'
),
(
    'Naruto vs Sasuke - Vale do Fim',
    (SELECT IdArco FROM Arcos WHERE Nome = 'Missao de Recuperacao de Sasuke'),
    'Vale do Fim',
    'Sasuke vence e deixa a vila da folha'
),
(
    'Kakashi vs Zabuza - Primeiro Confronto',
    (SELECT IdArco FROM Arcos WHERE Nome = 'Pais das Ondas'),
    'Floresta próxima à ponte',
    'Zabuza recua após intervenção da Equipe 7'
),
(
    'Itachi e Kisame vs Kakashi, Asuma e Kurenai',
    (SELECT IdArco FROM Arcos WHERE Nome = 'Busca por Tsunade'),
    'Entrada da Vila da Folha',
    'Kakashi é derrotado por Tsukuyomi'
),
(
    'Jiraiya vs Itachi e Kisame',
    (SELECT IdArco FROM Arcos WHERE Nome = 'Busca por Tsunade'),
    'Hotel onde Naruto estava hospedado',
    'Itachi e Kisame recuam'
),
(
    'Naruto vs Sasuke - Hospital',
    (SELECT IdArco FROM Arcos WHERE Nome = 'Busca por Tsunade'),
    'Telhado do Hospital de Konoha',
    'Luta interrompida por Kakashi'
),
(
    'Neji vs Hinata',
    (SELECT IdArco FROM Arcos WHERE Nome = 'Exame Chunin'),
    'Arena do Exame Chunin',
    'Neji vence e Hinata fica gravemente ferida'
),
(
    'Shikamaru vs Temari',
    (SELECT IdArco FROM Arcos WHERE Nome = 'Exame Chunin'),
    'Arena do Exame Chunin',
    'Shikamaru vence mas desiste'
)
''')

cursor.execute('''
INSERT INTO ConfrontoParticipantes VALUES
               
((SELECT IdConfronto FROM Confrontos WHERE Descricao = 'Naruto vs Neji'),
 (SELECT IdPersonagem FROM Personagens WHERE Nome = 'Naruto'),
 'Combatente','Vencedor'),
((SELECT IdConfronto FROM Confrontos WHERE Descricao = 'Naruto vs Neji'),
 (SELECT IdPersonagem FROM Personagens WHERE Nome = 'Neji'),
 'Combatente','Derrotado'),
               
((SELECT IdConfronto FROM Confrontos WHERE Descricao = 'Rock Lee vs Gaara'),
 (SELECT IdPersonagem FROM Personagens WHERE Nome = 'Rock'),
 'Combatente','Derrotado'),
((SELECT IdConfronto FROM Confrontos WHERE Descricao = 'Rock Lee vs Gaara'),
 (SELECT IdPersonagem FROM Personagens WHERE Nome = 'Gaara'),
 'Combatente','Vencedor'),

((SELECT IdConfronto FROM Confrontos WHERE Descricao = 'Naruto e Sasuke vs Haku'),
 (SELECT IdPersonagem FROM Personagens WHERE Nome = 'Naruto'),
 'Combatente','Sobreviveu'),
((SELECT IdConfronto FROM Confrontos WHERE Descricao = 'Naruto e Sasuke vs Haku'),
 (SELECT IdPersonagem FROM Personagens WHERE Nome = 'Sasuke'),
 'Combatente','Sobreviveu'),
((SELECT IdConfronto FROM Confrontos WHERE Descricao = 'Naruto e Sasuke vs Haku'),
 (SELECT IdPersonagem FROM Personagens WHERE Nome = 'Haku'),
 'Combatente','Morreu'),
            
((SELECT IdConfronto FROM Confrontos WHERE Descricao = 'Hiruzen vs Orochimaru'),
 (SELECT IdPersonagem FROM Personagens WHERE Nome = 'Hiruzen'),
 'Combatente','Morreu'),
((SELECT IdConfronto FROM Confrontos WHERE Descricao = 'Hiruzen vs Orochimaru'),
 (SELECT IdPersonagem FROM Personagens WHERE Nome = 'Orochimaru'),
 'Combatente','Sobreviveu'),

((SELECT IdConfronto FROM Confrontos WHERE Descricao = 'Naruto vs Gaara'),
 (SELECT IdPersonagem FROM Personagens WHERE Nome = 'Naruto'),
 'Combatente','Vencedor'),
((SELECT IdConfronto FROM Confrontos WHERE Descricao = 'Naruto vs Gaara'),
 (SELECT IdPersonagem FROM Personagens WHERE Nome = 'Gaara'),
 'Combatente','Derrotado'),

((SELECT IdConfronto FROM Confrontos WHERE Descricao = 'Naruto vs Sasuke - Vale do Fim'),
 (SELECT IdPersonagem FROM Personagens WHERE Nome = 'Naruto'),
 'Combatente','Derrotado'),

((SELECT IdConfronto FROM Confrontos WHERE Descricao = 'Naruto vs Sasuke - Vale do Fim'),
 (SELECT IdPersonagem FROM Personagens WHERE Nome = 'Sasuke'),
 'Combatente','Vencedor'),

((SELECT IdConfronto FROM Confrontos WHERE Descricao = 'Kakashi vs Zabuza - Primeiro Confronto'),
 (SELECT IdPersonagem FROM Personagens WHERE Nome = 'Kakashi'),
 'Combatente','Sobreviveu'),
((SELECT IdConfronto FROM Confrontos WHERE Descricao = 'Kakashi vs Zabuza - Primeiro Confronto'),
 (SELECT IdPersonagem FROM Personagens WHERE Nome = 'Zabuza'),
 'Combatente','Fugiu'),

((SELECT IdConfronto FROM Confrontos WHERE Descricao = 'Itachi e Kisame vs Kakashi, Asuma e Kurenai'),
 (SELECT IdPersonagem FROM Personagens WHERE Nome = 'Itachi'),
 'Combatente','Vencedor'),
((SELECT IdConfronto FROM Confrontos WHERE Descricao = 'Itachi e Kisame vs Kakashi, Asuma e Kurenai'),
 (SELECT IdPersonagem FROM Personagens WHERE Nome = 'Kisame'),
 'Combatente','Vencedor'),
((SELECT IdConfronto FROM Confrontos WHERE Descricao = 'Itachi e Kisame vs Kakashi, Asuma e Kurenai'),
 (SELECT IdPersonagem FROM Personagens WHERE Nome = 'Kakashi'),
 'Combatente','Derrotado'),
((SELECT IdConfronto FROM Confrontos WHERE Descricao = 'Itachi e Kisame vs Kakashi, Asuma e Kurenai'),
 (SELECT IdPersonagem FROM Personagens WHERE Nome = 'Asuma'),
 'Combatente','Sobreviveu'),
((SELECT IdConfronto FROM Confrontos WHERE Descricao = 'Itachi e Kisame vs Kakashi, Asuma e Kurenai'),
 (SELECT IdPersonagem FROM Personagens WHERE Nome = 'Kurenai'),
 'Combatente','Sobreviveu'),
               
((SELECT IdConfronto FROM Confrontos WHERE Descricao = 'Jiraiya vs Itachi e Kisame'),
 (SELECT IdPersonagem FROM Personagens WHERE Nome = 'Jiraiya'),
 'Combatente','Vencedor'),
((SELECT IdConfronto FROM Confrontos WHERE Descricao = 'Jiraiya vs Itachi e Kisame'),
 (SELECT IdPersonagem FROM Personagens WHERE Nome = 'Itachi'),
 'Combatente','Fugiu'),
((SELECT IdConfronto FROM Confrontos WHERE Descricao = 'Jiraiya vs Itachi e Kisame'),
 (SELECT IdPersonagem FROM Personagens WHERE Nome = 'Kisame'),
 'Combatente','Fugiu'),

((SELECT IdConfronto FROM Confrontos WHERE Descricao = 'Naruto vs Sasuke - Hospital'),
 (SELECT IdPersonagem FROM Personagens WHERE Nome = 'Naruto'),
 'Combatente','Empate'),

((SELECT IdConfronto FROM Confrontos WHERE Descricao = 'Naruto vs Sasuke - Hospital'),
 (SELECT IdPersonagem FROM Personagens WHERE Nome = 'Sasuke'),
 'Combatente','Empate'),

((SELECT IdConfronto FROM Confrontos WHERE Descricao = 'Neji vs Hinata'),
 (SELECT IdPersonagem FROM Personagens WHERE Nome = 'Neji'),
 'Combatente','Vencedor'),
((SELECT IdConfronto FROM Confrontos WHERE Descricao = 'Neji vs Hinata'),
 (SELECT IdPersonagem FROM Personagens WHERE Nome = 'Hinata'),
 'Combatente','Derrotado'),

((SELECT IdConfronto FROM Confrontos WHERE Descricao = 'Shikamaru vs Temari'),
 (SELECT IdPersonagem FROM Personagens WHERE Nome = 'Shikamaru'),
 'Combatente','Vencedor'),

((SELECT IdConfronto FROM Confrontos WHERE Descricao = 'Shikamaru vs Temari'),
 (SELECT IdPersonagem FROM Personagens WHERE Nome = 'Temari'),
 'Combatente','Derrotado')
;               
''')

conn.commit()