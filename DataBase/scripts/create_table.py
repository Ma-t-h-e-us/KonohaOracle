from ..databaseConfig import cursor, conn

cursor.execute("""
DROP TABLE IF EXISTS 
PersonagensAtributosDatabook,
PersonagensHabilidades,
Habilidades,
Databooks,
PersonagensElementos,
PersonagensJutsus,
Jutsus,
Personagens,
Elementos,
TiposJutsu,
TiposElementos,
Ocupacoes,
Vilas,
Arcos,
Clas,
TipoPersonagens
CASCADE;
""")

cursor.execute('''
CREATE TABLE TipoPersonagens (
    IdTipoPersonagem INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    Relevancia VARCHAR(20) NOT NULL
)
''')

cursor.execute('''
CREATE TABLE Clas (
    IdCla INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Descricao VARCHAR(200)
)
''')

cursor.execute('''
CREATE TABLE Arcos (
    IdArco INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Descricao VARCHAR(200)
)
''')

cursor.execute('''
CREATE TABLE Vilas (
    IdVila INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Pais VARCHAR(20) NOT NULL
)
''')

cursor.execute('''
CREATE TABLE Ocupacoes (
    IdOcupacao INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    Nome VARCHAR(30) NOT NULL
)
''')

cursor.execute('''
CREATE TABLE TiposElementos (
    IdTiposElementos INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    Nome VARCHAR(50) NOT NULL
)
''')

cursor.execute('''
CREATE TABLE TiposJutsu (
    IdTipoJutsu INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    Nome VARCHAR(30) NOT NULL
)
''')

cursor.execute('''
CREATE TABLE Elementos (
    IdElemento INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    IdTiposElementos INT,
    Nome VARCHAR(30) NOT NULL,
    CONSTRAINT fk_elemento_tipo
        FOREIGN KEY (IdTiposElementos)
        REFERENCES TiposElementos (IdTiposElementos)
        ON DELETE SET NULL
)
''')

cursor.execute('''
CREATE TABLE Personagens (
    IdPersonagem INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    IdTipoPersonagem INT NOT NULL,
    IdCla INT,
    IdArcoAparicao INT NOT NULL,
    IdArcoMorte INT,
    IdOcupacaoClassico INT,
    IdOcupacaoShippuden INT,
    IdVila INT,

    Nome VARCHAR(100) NOT NULL,
    Sobrenome VARCHAR(100),
    IdadeClasico INT,
    IdadeShippuden INT,

    Sexo VARCHAR(10) NOT NULL
        CHECK (Sexo IN ('Masculino', 'Feminino')),

    DataNascimento DATE,
    AlturaClassico DECIMAL(5,2),
    AlturaShippuden DECIMAL(5,2),
    CorCabelo VARCHAR(50),
    CorOlhos VARCHAR(50),
    CorPele VARCHAR(50),
    DescricaoRoupaClassico VARCHAR(200),
    DescricaoRoupaShippuden VARCHAR(200),

    MissoesCompletas INT,

    Descricao VARCHAR(250),
    HistoriaPersonagem TEXT,

    Estado VARCHAR(10) NOT NULL
        CHECK (Estado IN ('Vivo', 'Morto')),

    FOREIGN KEY (IdTipoPersonagem)
        REFERENCES TipoPersonagens (IdTipoPersonagem),

    FOREIGN KEY (IdCla)
        REFERENCES Clas (IdCla),

    FOREIGN KEY (IdArcoAparicao)
        REFERENCES Arcos (IdArco),

    FOREIGN KEY (IdArcoMorte)
        REFERENCES Arcos (IdArco),

    FOREIGN KEY (IdOcupacaoClassico)
        REFERENCES Ocupacoes (IdOcupacao),

    FOREIGN KEY (IdOcupacaoShippuden)
        REFERENCES Ocupacoes (IdOcupacao),

    FOREIGN KEY (IdVila)
        REFERENCES Vilas (IdVila)
)
''')

cursor.execute('''
CREATE TABLE Jutsus (
    IdJutsu INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    IdElemento INT,
    IdTipoJutsu INT NOT NULL,

    Nome VARCHAR(100) NOT NULL,
    Descricao VARCHAR(120),

    Rank VARCHAR(2)
        CHECK (Rank IN ('S','A','B','C','D')),

    FOREIGN KEY (IdElemento)
        REFERENCES Elementos (IdElemento),

    FOREIGN KEY (IdTipoJutsu)
        REFERENCES TiposJutsu (IdTipoJutsu)
)
''')

cursor.execute('''
CREATE TABLE PersonagensJutsus (
    IdPersonagem INT,
    IdJutsu INT,
    PRIMARY KEY (IdPersonagem, IdJutsu),

    FOREIGN KEY (IdPersonagem)
        REFERENCES Personagens (IdPersonagem)
        ON DELETE CASCADE,

    FOREIGN KEY (IdJutsu)
        REFERENCES Jutsus (IdJutsu)
        ON DELETE CASCADE
)
''')

cursor.execute('''
CREATE TABLE PersonagensElementos (
    IdPersonagem INT,
    IdElemento INT,
    PRIMARY KEY (IdPersonagem, IdElemento),

    FOREIGN KEY (IdPersonagem)
        REFERENCES Personagens (IdPersonagem)
        ON DELETE CASCADE,

    FOREIGN KEY (IdElemento)
        REFERENCES Elementos (IdElemento)
        ON DELETE CASCADE
)
''')

cursor.execute('''
CREATE TABLE Habilidades (
    IdHabilidade INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Descricao VARCHAR(150)
);
''')

cursor.execute('''
CREATE TABLE PersonagensHabilidades (
    IdPersonagem INT,
    IdHabilidade INT,

    PRIMARY KEY (IdPersonagem, IdHabilidade),

    FOREIGN KEY (IdPersonagem)
        REFERENCES Personagens (IdPersonagem)
        ON DELETE CASCADE,

    FOREIGN KEY (IdHabilidade)
        REFERENCES Habilidades (IdHabilidade)
        ON DELETE CASCADE
);
''')

cursor.execute('''
CREATE TABLE Databooks (
    IdDatabook INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    Edicao INT NOT NULL CHECK (Edicao >= 1 AND Edicao <= 4) UNIQUE,
    Descricao VARCHAR(100)
);
''')

cursor.execute('''
CREATE TABLE PersonagensAtributosDatabook (
    IdPersonagem INT,
    IdDatabook INT,

    Ninjutsu DECIMAL(2,1) NOT NULL CHECK (Ninjutsu >= 0 AND Ninjutsu <= 5),
    Taijutsu DECIMAL(2,1) NOT NULL CHECK (Taijutsu >= 0 AND Taijutsu <= 5),
    Genjutsu DECIMAL(2,1) NOT NULL CHECK (Genjutsu >= 0 AND Genjutsu <= 5),
    Inteligencia DECIMAL(2,1) NOT NULL CHECK (Inteligencia >= 0 AND Inteligencia <= 5),
    Forca DECIMAL(2,1) NOT NULL CHECK (Forca >= 0 AND Forca <= 5),
    Agilidade DECIMAL(2,1) NOT NULL CHECK (Agilidade >= 0 AND Agilidade <= 5),
    Estamina DECIMAL(2,1) NOT NULL CHECK (Estamina >= 0 AND Estamina <= 5),
    SelosManuais DECIMAL(2,1) NOT NULL CHECK (SelosManuais >= 0 AND SelosManuais <= 5),
        Total DECIMAL(4,1) GENERATED ALWAYS AS (
        Ninjutsu +
        Taijutsu +
        Genjutsu +
        Inteligencia +
        Forca +
        Agilidade +
        Estamina +
        SelosManuais
    ) STORED,

    PRIMARY KEY (IdPersonagem, IdDatabook),

    FOREIGN KEY (IdPersonagem)
        REFERENCES Personagens (IdPersonagem)
        ON DELETE CASCADE,

    FOREIGN KEY (IdDatabook)
        REFERENCES Databooks (IdDatabook)
        ON DELETE CASCADE
);
''')

conn.commit()