from DataBase.databaseConfig import cursor, conn

personagens = [

    # ======================
    # GENINS
    # ======================

    (4,16,1,None,1,2,1,'Hinata Hyuga',12,16,'Feminino','1988-12-27',1.60,'Preto','Branco','Clara',5,'Herdeira do cla Hyuga e usuaria do Byakugan.','Vivo'),
    (4,21,1,None,1,2,1,'Shino Aburame',12,16,'Masculino','1988-01-23',1.63,'Preto','Escuro','Clara',5,'Membro do cla Aburame que utiliza insetos.','Vivo'),
    (4,22,1,None,1,2,1,'Kiba Inuzuka',12,16,'Masculino','1988-07-07',1.65,'Castanho','Preto','Clara',5,'Ninja que luta ao lado de seu parceiro canino.','Vivo'),
    (4,18,1,None,1,2,1,'Shikamaru Nara',12,16,'Masculino','1987-09-22',1.70,'Preto','Preto','Clara',10,'Genio estrategista que manipula sombras.','Vivo'),
    (4,20,1,None,1,2,1,'Ino Yamanaka',12,16,'Feminino','1988-09-23',1.62,'Loiro','Azul','Clara',6,'Especialista em tecnicas mentais.','Vivo'),
    (4,19,1,None,1,2,1,'Choji Akimichi',12,16,'Masculino','1987-05-01',1.68,'Castanho','Preto','Clara',6,'Utiliza tecnicas de expansao corporal.','Vivo'),
    (4,16,1,None,1,3,1,'Neji Hyuga',13,17,'Masculino','1986-07-03',1.72,'Preto','Branco','Clara',15,'Prodigio do cla Hyuga.','Morto'),
    (4,None,1,None,1,3,1,'Rock Lee',13,17,'Masculino','1986-11-27',1.72,'Preto','Preto','Clara',12,'Especialista em Taijutsu.','Vivo'),
    (4,None,1,None,1,2,1,'Tenten',13,17,'Feminino','1986-03-09',1.65,'Castanho','Castanho','Clara',8,'Especialista em armas ninja.','Vivo'),

    # ======================
    # SENSEIS
    # ======================

    (4,None,1,None,3,3,1,'Might Guy',26,30,'Masculino','1962-01-01',1.84,'Preto','Preto','Clara',500,'Especialista supremo em Taijutsu.','Vivo'),
    (4,17,1,None,3,3,1,'Asuma Sarutobi',27,31,'Masculino','1965-10-18',1.90,'Castanho','Castanho','Clara',600,'Jounin e filho do Terceiro Hokage.','Morto'),
    (4,None,1,None,3,3,1,'Kurenai Yuhi',27,31,'Feminino','1967-06-11',1.69,'Preto','Vermelho','Clara',400,'Especialista em Genjutsu.','Vivo'),

    # ======================
    # SANNIN
    # ======================

    (4,None,5,None,3,3,1,'Jiraiya',50,54,'Masculino','1954-11-11',1.91,'Branco','Preto','Clara',2000,'Um dos Tres Sannin Lendarios.','Morto'),
    (1,15,5,None,5,5,1,'Tsunade Senju',51,55,'Feminino','1951-08-02',1.63,'Loiro','Castanho','Clara',1500,'Quinta Hokage.','Vivo'),
    (3,None,4,None,3,3,11,'Orochimaru',50,54,'Masculino','1954-10-27',1.79,'Preto','Amarelo','Clara',1800,'Ex membro da Akatsuki e Sannin.','Vivo'),

    # ======================
    # AKATSUKI
    # ======================

    (3,3,3,None,3,3,1,'Itachi Uchiha',18,21,'Masculino','1985-06-09',1.78,'Preto','Vermelho','Clara',200,'Membro da Akatsuki e genio em genjutsu.','Morto'),
    (3,24,3,None,3,3,3,'Kisame Hoshigaki',29,32,'Masculino','1980-03-18',1.95,'Azul','Preto','Azulada',150,'Espadachim da Nevoa e membro da Akatsuki.','Morto'),

    # ======================
    # VILOES DO SOM
    # ======================

    (3,None,6,None,3,3,11,'Kimimaro',15,None,'Masculino','1988-06-15',1.66,'Branco','Verde','Clara',20,'Ultimo sobrevivente do cla Kaguya.','Morto'),
    (3,None,6,None,3,3,11,'Tayuya',14,None,'Feminino','1989-05-18',1.48,'Vermelho','Castanho','Clara',10,'Usuaria de flauta.','Morto'),
    (3,None,6,None,3,3,11,'Sakon',14,None,'Masculino','1989-07-20',1.55,'Cinza','Preto','Clara',10,'Membro do Quarteto do Som.','Morto'),
    (3,None,6,None,3,3,11,'Ukon',14,None,'Masculino','1989-07-20',1.55,'Cinza','Preto','Clara',10,'Irmao de Sakon.','Morto'),
    (3,None,6,None,3,3,11,'Kidomaru',14,None,'Masculino','1989-12-16',1.59,'Castanho','Preto','Clara',10,'Especialista em teias.','Morto'),
    (3,None,6,None,3,3,11,'Jirobo',14,None,'Masculino','1989-01-10',1.78,'Laranja','Preto','Clara',10,'Especialista em forca bruta.','Morto'),

    # ======================
    # AREIA
    # ======================

    (4,None,3,None,1,6,2,'Gaara',12,16,'Masculino','1988-01-19',1.66,'Vermelho','Verde','Clara',50,'Jinchuuriki do Shukaku.','Vivo'),
    (4,None,3,None,1,3,2,'Temari',15,19,'Feminino','1985-08-23',1.65,'Loiro','Verde','Clara',40,'Especialista em vento.','Vivo'),
    (4,None,3,None,1,3,2,'Kankuro',14,18,'Masculino','1986-05-15',1.67,'Preto','Preto','Clara',40,'Marionetista da Areia.','Vivo'),
    (4,None,3,None,3,3,2,'Baki',30,None,'Masculino','1965-02-02',1.82,'Preto','Preto','Clara',300,'Jounin estrategista da Areia.','Vivo'),

    # ======================
    # INVOCACOES
    # ======================

    (4,None,2,None,11,11,1,'Gamabunta',None,None,'Masculino','1900-01-01',5.00,'Verde','Amarelo','Verde',200,'Rei dos Sapos.','Vivo'),
    (4,None,1,None,11,11,1,'Pakkun',None,None,'Masculino','1900-01-01',0.40,'Marrom','Preto','Marrom',150,'Cao ninja invocado por Kakashi.','Vivo'),
    (4,22,1,None,11,11,1,'Akamaru',None,None,'Masculino','1900-01-01',0.50,'Branco','Preto','Branco',100,'Companheiro canino de Kiba.','Vivo'),
]

sql = """
INSERT INTO Personagens (
    IdTipoPersonagem, IdCla, IdArcoAparicao, IdArcoMorte,
    IdOcupacaoClassico, IdOcupacaoShippuden,
    IdVila, Nome, Idade_Clasico, Idade_Shippuden,
    Sexo, DataNascimento, Altura,
    CorCabelo, CorOlhos, CorPele,
    MissoesCompletas, Descricao, Estado
) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

cursor.executemany(sql, personagens)
conn.commit()

print("Seed de personagens executado com sucesso.")