from ..databaseConfig import cursor, conn

#Criação de tabelas do bd
cursor.execute('''
CREATE TABLE TipoPersonagens (
    IdTipoPersonagem INT AUTO_INCREMENT PRIMARY KEY,
    Relevancia VARCHAR(20) NOT NULL
        CHECK (Relevancia IN (
            'Protagonista',
            'Deutragonista',
            'Antagonista',
            'Principais',
            'Secundarios',
            'Terciario'
        ))
)
''')

cursor.execute('''
CREATE TABLE Clas (
    IdCla INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Descricao VARCHAR(150)
)    
''')

cursor.execute('''
CREATE TABLE Arcos (
    IdArco INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Descricao VARCHAR(200)
)
''')

cursor.execute('''
CREATE TABLE Vilas (
    IdVila INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Pais VARCHAR(20) NOT NULL
        CHECK (Pais IN (
            'Fogo','Terra','Agua','Vento','Relampago',
            'Ferro','Som','Chuva','Grama'
        ))
)
''')

cursor.execute('''
CREATE TABLE Ocupacoes (
    IdOcupacao INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(30) NOT NULL
        CHECK (Nome IN (
            'Genin','Chunin','Jounin','Jounin especial',
            'Hokage','Kazekage','Mizukage','Raikage',
            'Tsuchikage','Civil','Animal'
        ))
)
''')

cursor.execute('''
CREATE TABLE TiposElementos (
    IdTiposElementos INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(50) NOT NULL
)
''')

cursor.execute('''
CREATE TABLE TiposJutsu (
    IdTipoJutsu INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(30) NOT NULL
        CHECK (Nome IN (
            'Taijutsu','Genjutsu','Ninjutsu',
            'Fuuinjutsu','Ninjutsu Medico',
            'Kinjutsu','Nenhum'
        ))
)
''')

cursor.execute('''
CREATE TABLE Elementos (
    IdElemento INT AUTO_INCREMENT PRIMARY KEY,
    IdTiposElementos INT,
    Nome VARCHAR(30) NOT NULL
        CHECK (Nome IN (
            'Fogo','Agua','Terra','Relampago','Vento',
            'Yin-Yang','Nenhum','Gelo','Poeira',
            'Explosao','Lava','Vapor'
        )),
    CONSTRAINT fk_elemento_tipo
        FOREIGN KEY (IdTiposElementos)
        REFERENCES TiposElementos (IdTiposElementos)
)
''')

cursor.execute('''
CREATE TABLE Personagens (
    IdPersonagem INT AUTO_INCREMENT PRIMARY KEY,
    IdTipoPersonagem INT NOT NULL,
    IdCla INT,
    IdArcoAparicao INT NOT NULL,
    IdArcoMorte INT,
    IdOcupacaoClassico INT,
    IdOcupacaoShippuden INT,
    IdVila INT,

    Nome VARCHAR(100) NOT NULL,
    Idade_Clasico INT,
    Idade_Shippuden INT,

    Sexo VARCHAR(10) NOT NULL
        CHECK (Sexo IN ('Masculino', 'Feminino')),

    DataNascimento DATE,
    Altura DECIMAL(5,2),
    CorCabelo VARCHAR(50),
    CorOlhos VARCHAR(50),
    CorPele VARCHAR(50),

    MissoesCompletas INT
        CHECK (MissoesCompletas >= 0 AND MissoesCompletas < 10000),

    Descricao VARCHAR(250),

    Estado VARCHAR(10) NOT NULL
        CHECK (Estado IN ('Vivo', 'Morto')),

    CONSTRAINT fk_personagem_tipo
        FOREIGN KEY (IdTipoPersonagem)
        REFERENCES TipoPersonagens (IdTipoPersonagem),

    CONSTRAINT fk_personagem_cla
        FOREIGN KEY (IdCla)
        REFERENCES Clas (IdCla),

    CONSTRAINT fk_personagem_arco_aparicao
        FOREIGN KEY (IdArcoAparicao)
        REFERENCES Arcos (IdArco),

    CONSTRAINT fk_personagem_arco_morte
        FOREIGN KEY (IdArcoMorte)
        REFERENCES Arcos (IdArco),

    CONSTRAINT fk_personagem_ocupacao_classico
        FOREIGN KEY (IdOcupacaoClassico)
        REFERENCES Ocupacoes (IdOcupacao),

    CONSTRAINT fk_personagem_ocupacao_shippuden
        FOREIGN KEY (IdOcupacaoShippuden)
        REFERENCES Ocupacoes (IdOcupacao),

    CONSTRAINT fk_personagem_vila
        FOREIGN KEY (IdVila)
        REFERENCES Vilas (IdVila)
)
''')

cursor.execute('''
CREATE TABLE Jutsus (
    IdJutsu INT AUTO_INCREMENT PRIMARY KEY,
    IdElemento INT,
    IdTipoJutsu INT NOT NULL,

    Nome VARCHAR(100) NOT NULL,
    Descricao VARCHAR(120),

    Rank VARCHAR(2) NOT NULL
        CHECK (Rank IN ('S','A','B','C','D')),

    CONSTRAINT fk_jutsu_elemento
        FOREIGN KEY (IdElemento)
        REFERENCES Elementos (IdElemento),

    CONSTRAINT fk_jutsu_tipo
        FOREIGN KEY (IdTipoJutsu)
        REFERENCES TiposJutsu (IdTipoJutsu)
)
''')

cursor.execute('''
CREATE TABLE PersonagensJutsus (
    IdPersonagem INT,
    IdJutsu INT,
    PRIMARY KEY (IdPersonagem, IdJutsu),

    CONSTRAINT fk_pj_personagem
        FOREIGN KEY (IdPersonagem)
        REFERENCES Personagens (IdPersonagem),

    CONSTRAINT fk_pj_jutsu
        FOREIGN KEY (IdJutsu)
        REFERENCES Jutsus (IdJutsu)
)
''')

cursor.execute('''
CREATE TABLE PersonagensElementos (
    IdPersonagem INT,
    IdElemento INT,
    PRIMARY KEY (IdPersonagem, IdElemento),

    CONSTRAINT fk_pe_personagem
        FOREIGN KEY (IdPersonagem)
        REFERENCES Personagens (IdPersonagem),

    CONSTRAINT fk_pe_elemento
        FOREIGN KEY (IdElemento)
        REFERENCES Elementos (IdElemento)
)
''')

conn.commit()