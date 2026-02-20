from DataBase.databaseConfig import cursor, conn

#Adicionar ocupacoes
cursor.execute('''
INSERT INTO Ocupacoes (Nome) VALUES
('Anbu'),
('Conselheiro'),
('Sannin'),
('Jounin Especial')
''')

#Acicionar habilidades
cursor.execute('''
INSERT INTO Habilidades (Nome, Descricao) VALUES
('Modo Sabio','Capacidade de absorver energia natural e aumentar drasticamente atributos fisicos e sensoriais.'),
('Sharingan','Dojutsu do cla Uchiha que permite copiar jutsus, prever movimentos e lancar genjutsus.'),
('Byakugan','Dojutsu do cla Hyuga que concede visao de 360 graus e percepcao do fluxo de chakra.'),
('Marca da Maldicao','Selo que aumenta o poder do usuario ao custo de consumir seu chakra e afetar seu corpo.'),
('Ninjutsu Medico','Tecnicas medicas que utilizam chakra para curar ferimentos e realizar procedimentos complexos.'),
('Olfato Agucado','Capacidade sensorial avancada de rastrear pessoas e identificar odores a longa distancia.'),
('Vigor Fisico Elevado','Grande resistencia fisica e capacidade de lutar por longos periodos sem exaustao.'),
('Experiencia em Combate','Amplo historico de batalhas que proporciona estrategia e adaptacao em confronto.'),
('Frieza','Capacidade de manter a calma e agir racionalmente mesmo sob extrema pressao.'),
('Criador de Jutsus','Habilidade de desenvolver tecnicas originais e inovadoras.'),
('Mestre em Taijutsu','Dominio avancado de tecnicas de combate corpo a corpo sem uso de ninjutsu.'),
('Especialista em Genjutsu','Alta proficiencia em tecnicas ilusorias capazes de manipular os sentidos do oponente.'),
('Mestre em Kenjutsu','Grande habilidade no uso de espadas e armas laminadas em combate.'),
('Combate a Longa Distancia','Especialista em ataques realizados a media e longa distancia com alta precisao.'),
('Lideranca','Capacidade de comandar equipes e coordenar estrategias em missao ou batalha.'),
('Manipulacao Psicologica','Habilidade de influenciar emocional e mentalmente adversarios ou aliados.'),
('Ninja Sensorial','Capacidade de detectar presencas e fluxos de chakra em grandes areas.'),
('Rastreamento Avancado','Especialista em localizar alvos por vestigios fisicos ou chakra.'),
('Regeneracao Acelerada','Recuperacao rapida de ferimentos durante ou apos combates.'),
('Jinchuuriki','Portador de uma Bijuu selada em seu corpo.'),
('Modo Bijuu','Capacidade de utilizar o poder da Bijuu de forma controlada.'),
('Imortalidade','Incapacidade de morrer por meios convencionais ou envelhecimento natural.'),
('Espionagem','Especialista em coleta de informacoes de forma furtiva e estrategica.');
''')


#Personagens faltantes
#TIME 11
cursor.execute('''
INSERT INTO Personagens (
    IdTipoPersonagem,
    IdCla,
    IdArcoAparicao,
    IdArcoMorte,
    IdOcupacaoClassico,
    IdOcupacaoShippuden,
    IdVila,
    Nome,
    Sobrenome,
    IdadeClasico,
    IdadeShippuden,
    Sexo,
    DataNascimento,
    AlturaClassico,
    AlturaShippuden,
    CorCabelo,
    CorOlhos,
    CorPele,
    DescricaoRoupaClassico,
    DescricaoRoupaShippuden,
    MissoesCompletas,
    Descricao,
    HistoriaPersonagem,
    Estado
)
VALUES

-- HIRUZEN SARUTOBI
(
    (SELECT IdTipoPersonagem FROM TipoPersonagens WHERE Relevancia = 'Secundarios'),
    (SELECT IdCla FROM Clas WHERE Nome = 'Sarutobi'),
    (SELECT IdArco FROM Arcos WHERE Nome = 'Prologo'),
    (SELECT IdArco FROM Arcos WHERE Nome = 'Ataque a Vila da Folha'),
    (SELECT IdOcupacao FROM Ocupacoes WHERE Nome = 'Hokage'),
    NULL,
    (SELECT IdVila FROM Vilas WHERE Nome = 'Vila Oculta da Folha'),
    'Hiruzen',
    'Sarutobi',
    68,
    NULL,
    'Masculino',
    '1937-02-08',
    1.63,
    NULL,
    'Branco',
    'Preto',
    'Clara',
    'Manto tradicional do Hokage com chapeu cerimonial e cachimbo.',
    NULL,
    1829,
    'Terceiro Hokage conhecido como O Professor.',
    'Hiruzen Sarutobi foi o Terceiro Hokage e mestre dos Sannin Lendarios. Sacrificou sua vida para proteger Konoha durante o Ataque a Vila da Folha.',
    'Morto'
),

-- JIRAIYA
(
    (SELECT IdTipoPersonagem FROM TipoPersonagens WHERE Relevancia = 'Principais'),
    NULL,
    (SELECT IdArco FROM Arcos WHERE Nome = 'Exame Chunin'),
    (SELECT IdArco FROM Arcos WHERE Nome = 'Historia de Jiraiya, o Destemido'),
    (SELECT IdOcupacao FROM Ocupacoes WHERE Nome = 'Sannin'),
    (SELECT IdOcupacao FROM Ocupacoes WHERE Nome = 'Sannin'),
    (SELECT IdVila FROM Vilas WHERE Nome = 'Vila Oculta da Folha'),
    'Jiraiya',
    NULL,
    50,
    54,
    'Masculino',
    '1954-11-11',
    1.91,
    1.91,
    'Branco',
    'Preto',
    'Clara',
    'Traje vermelho tradicional com pergaminho nas costas.',
    'Traje vermelho tradicional com pergaminho nas costas.',
    1839,
    'Um dos Tres Sannin Lendarios.',
    'Aluno de Hiruzen e membro dos Sannin Lendarios, conhecido como Sapo Sábio da Montanha, ou Sábio Tarado. Morreu investigando Pain na Vila da Chuva.',
    'Morto'
),

-- TSUNADE
(
    (SELECT IdTipoPersonagem FROM TipoPersonagens WHERE Relevancia = 'Secundarios'),
    (SELECT IdCla FROM Clas WHERE Nome = 'Senju'),
    (SELECT IdArco FROM Arcos WHERE Nome = 'Busca por Tsunade'),
    NULL,
    (SELECT IdOcupacao FROM Ocupacoes WHERE Nome = 'Sannin'),
    (SELECT IdOcupacao FROM Ocupacoes WHERE Nome = 'Hokage'),
    (SELECT IdVila FROM Vilas WHERE Nome = 'Vila Oculta da Folha'),
    'Tsunade',
    'Senju',
    51,
    55,
    'Feminino',
    '1955-08-02',
    1.63,
    1.63,
    'Loiro',
    'Castanho',
    'Clara',
    'Blusa verde com simbolo nas costas.',
    'Blusa verde com simbolo nas costas.',
    1256,
    'Uma das Tres Sannin Lendarias e Quinta Hokage.',
    'Neta do Primeiro Hokage, tornou-se Quinta Hokage liderando Konoha durante o enfrentamento a Akatsuki. Revolucionou o sistema ninja ao adionar um ninja medico em cada time.',
    'Vivo'
),

-- KOHARU UTATANE
(
    (SELECT IdTipoPersonagem FROM TipoPersonagens WHERE Relevancia = 'Terciario'),
    NULL,
    (SELECT IdArco FROM Arcos WHERE Nome = 'Exame Chunin'),
    NULL,
    (SELECT IdOcupacao FROM Ocupacoes WHERE Nome = 'Conselheiro'),
    (SELECT IdOcupacao FROM Ocupacoes WHERE Nome = 'Conselheiro'),
    (SELECT IdVila FROM Vilas WHERE Nome = 'Vila Oculta da Folha'),
    'Koharu',
    'Utatane',
    68,
    72,
    'Feminino',
    '1938-09-01',
    1.58,
    1.58,
    'Grisalho',
    'Preto',
    'Clara',
    'Roupas tradicionais de conselheira.',
    'Roupas tradicionais de conselheira.',
    NULL,
    'Membro do conselho de Konoha.',
    'Foi companheira de equipe de Hiruzen na juventude e tornou-se conselheira da Vila da Folha.',
    'Vivo'
),

-- HOMURA MITOKADO
(
    (SELECT IdTipoPersonagem FROM TipoPersonagens WHERE Relevancia = 'Terciario'),
    NULL,
    (SELECT IdArco FROM Arcos WHERE Nome = 'Exame Chunin'),
    NULL,
    (SELECT IdOcupacao FROM Ocupacoes WHERE Nome = 'Conselheiro'),
    (SELECT IdOcupacao FROM Ocupacoes WHERE Nome = 'Conselheiro'),
    (SELECT IdVila FROM Vilas WHERE Nome = 'Vila Oculta da Folha'),
    'Homura',
    'Mitokado',
    68,
    72,
    'Masculino',
    '1938-10-08',
    1.65,
    1.65,
    'Grisalho',
    'Preto',
    'Clara',
    'Roupas tradicionais de conselheiro.',
    'Roupas tradicionais de conselheiro.',
    NULL,
    'Membro do conselho de Konoha.',
    'Foi companheiro de equipe de Hiruzen e posteriormente tornou-se conselheiro da Vila da Folha.',
    'Vivo'
);
''')

conn.commit()