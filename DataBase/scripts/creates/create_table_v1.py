from DataBase.databaseConfig import cursor, conn

cursor.execute('''
CREATE TABLE Invocacoes (
    IdInvocacao SERIAL PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL UNIQUE,
    TipoInvocacao VARCHAR(50),
    LocalOrigem VARCHAR(100),
    Descricao TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE ContratoInvocacao (
    IdPersonagem INT NOT NULL,
    IdInvocacao INT NOT NULL,

    PRIMARY KEY (IdPersonagem, IdInvocacao),

    FOREIGN KEY (IdPersonagem)
        REFERENCES Personagens(IdPersonagem)
        ON DELETE CASCADE,

    FOREIGN KEY (IdInvocacao)
        REFERENCES Invocacoes(IdInvocacao)
        ON DELETE CASCADE
);
''')

cursor.execute('''
CREATE TABLE Confrontos (
    IdConfronto SERIAL PRIMARY KEY,
    Descricao TEXT NOT NULL,
    IdArco INT NOT NULL,
    Local VARCHAR(150),
    ResultadoDescricao TEXT,

    FOREIGN KEY (IdArco)
        REFERENCES Arcos(IdArco)
        ON DELETE CASCADE
);
''')

cursor.execute('''
CREATE TABLE ConfrontoParticipantes (
    IdConfronto INT NOT NULL,
    IdPersonagem INT NOT NULL,
    Papel VARCHAR(30) CHECK (Papel IN ('Suporte','Combatente','Invocacao')),
    Resultado VARCHAR(30) CHECK (Resultado IN ('Vencedor','Derrotado','Sobreviveu','Morreu','Fugiu','Empate')),

    PRIMARY KEY (IdConfronto, IdPersonagem),

    FOREIGN KEY (IdConfronto)
        REFERENCES Confrontos(IdConfronto)
        ON DELETE CASCADE,

    FOREIGN KEY (IdPersonagem)
        REFERENCES Personagens(IdPersonagem)
        ON DELETE CASCADE
);
''')

cursor.execute('''
CREATE TABLE Ferramentas (
    IdFerramenta SERIAL PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Descricao TEXT NOT NULL,
    Alcance VARCHAR(50) CHECK (
        Alcance IN (
            'Curto',
            'Medio',
            'Longo',
            'Variavel'
        )
    ),
    Unica BOOLEAN NOT NULL DEFAULT FALSE,
    Tipo VARCHAR(50) CHECK (
        Tipo IN (
            'Arma',
            'Arma Lendaria',
            'Explosivo',
            'Suporte',
            'Defensiva',
            'Selamento',
            'Cura'
        )
    ) NOT NULL
);
''')

cursor.execute('''
CREATE TABLE PersonagensFerramentas (
    IdPersonagem INT NOT NULL,
    IdFerramenta INT NOT NULL,

    PRIMARY KEY (IdPersonagem, IdFerramenta),

    FOREIGN KEY (IdPersonagem)
        REFERENCES Personagens(IdPersonagem)
        ON DELETE CASCADE,

    FOREIGN KEY (IdFerramenta)
        REFERENCES Ferramentas(IdFerramenta)
        ON DELETE CASCADE
);
''')

cursor.execute('''
CREATE TABLE Grupos (
    IdGrupo SERIAL PRIMARY KEY,
    Nome VARCHAR(120) NOT NULL UNIQUE,
    Descricao TEXT NOT NULL,
    Tipo VARCHAR(50) CHECK (
        Tipo IN (
            'Time',
            'Organizacao',
            'Divisao'
        )
    )
);
''')

cursor.execute('''
CREATE TABLE PersonagensGrupos (
    IdPersonagem INT NOT NULL,
    IdGrupo INT NOT NULL,
    Papel VARCHAR(50),

    PRIMARY KEY (IdPersonagem, IdGrupo),

    FOREIGN KEY (IdPersonagem)
        REFERENCES Personagens(IdPersonagem)
        ON DELETE CASCADE,

    FOREIGN KEY (IdGrupo)
        REFERENCES Grupos(IdGrupo)
        ON DELETE CASCADE
);
''')

conn.commit()