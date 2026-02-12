from ..databaseConfig import cursor, conn

cursor.execute("""
INSERT INTO Vilas (Nome, Pais) VALUES
('Vila do Ferro', 'Ferro'),
('Vila do Som', 'Som'),
('Vila da Chuva', 'Chuva'),
('Vila da Grama', 'Grama');
""")

cursor.execute("""
INSERT INTO Clas (Nome, Descricao) VALUES
('Senju', 'Clã lendário rival dos Uchiha, conhecido por sua vitalidade e liderança.'),
('Hyuga', 'Clã portador do Byakugan, especializado em combate corpo a corpo e controle de chakra.'),
('Sarutobi', 'Clã tradicional de Konoha, conhecido por sua versatilidade e lealdade.'),
('Nara', 'Clã estrategista especializado em técnicas de manipulação de sombras.'),
('Akimichi', 'Clã que utiliza técnicas de expansão corporal baseadas em calorias.'),
('Yamanaka', 'Clã especializado em técnicas mentais e transferência de consciência.'),
('Aburame', 'Clã que utiliza insetos como arma em combate.'),
('Inuzuka', 'Clã que luta em parceria com cães ninjas.'),
('Namikaze', 'Clã conhecido por grande velocidade e talento natural.'),
('Hoshigake', 'Clã da Névoa associado a grandes reservas de chakra e habilidades aquáticas.');
""")

cursor.execute("""
INSERT INTO Arcos (Nome, Descricao) VALUES
('Missao de Resgate do Kazekage', 'Akatsuki sequestra Gaara e o Time 7 parte para resgata-lo.'),
('Missao de Reconhecimento na Ponte Tenchi', 'Time Kakashi enfrenta Orochimaru e reencontra Sasuke.'),
('Missao de Supressao da Akatsuki', 'Shikamaru lidera equipe contra Hidan e Kakuzu.'),
('Missao de Busca por Itachi', 'Equipe formada para localizar Itachi Uchiha.'),
('Missao de Captura de Tres Caudas', 'Akatsuki tenta capturar o Sanbi.'),
('Perseguicao de Itachi', 'Sasuke rastreia Itachi para confronto final.'),
('Historia de Jiraiya, o Destemido', 'Jiraiya invade a vila da chuva para investigar Pain.'),
('Batalha Fadidica entre Irmaos', 'Confronto final entre Sasuke e Itachi.'),
('Invasao de Pain', 'Pain ataca Konoha em busca de Naruto.'),
('Cupula dos Cinco Kage', 'Reuniao das cinco grandes vilas ninja.'),
('Quarta Grande Guerra Ninja: Preparativos', 'Alianca Shinobi se organiza para guerra.'),
('Quarta Grande Guerra Ninja: Confronto', 'Grandes batalhas contra exercito de Zetsu e Edo Tensei'),
('Quarta Grande Guerra Ninja: Climax', 'Madara e Obito revelam plano final.'),
('Kaguya Otsutsuki e o Fim da Guerra', 'Naruto e Sasuke enfrentam Kaguya e encerram o conflito.');
""")

conn.commit()