from DataBase.databaseConfig import cursor, conn

cursor.execute('''
INSERT INTO Ferramentas (Nome, Descricao, Alcance, Unica, Tipo) VALUES

-- Armas básicas
('Kunai',
 'Adaga ninja versátil utilizada tanto para combate corpo a corpo quanto para arremesso.',
 'Curto',
 FALSE,
 'Arma'),

('Shuriken',
 'Estrela metálica afiada utilizada para ataques à distância.',
 'Medio',
 FALSE,
 'Arma'),

-- Explosivos
('Papel Bomba',
 'Etiqueta explosiva ativada com chakra que explode após um tempo determinado.',
 'Medio',
 FALSE,
 'Explosivo'),

('Bomba de Fumaca',
 'Dispositivo que libera uma cortina de fumaça para fuga ou distração.',
 'Curto',
 FALSE,
 'Suporte'),

-- Espadas Lendárias da Névoa
('Samehada',
 'Espada lendaria da Vila da Névoa que absorve chakra e possui consciência própria.',
 'Curto',
 TRUE,
 'Arma Lendaria'),

('Kubikiribocho',
 'Espada gigante que se regenera ao absorver ferro do sangue de suas vítimas.',
 'Curto',
 TRUE,
 'Arma Lendaria'),

-- Equipamentos do Susanoo de Itachi
('Espelho de Yata',
 'Escudo espiritual capaz de alterar sua natureza para defender qualquer ataque.',
 'Curto',
 TRUE,
 'Defensiva'),

('Espada Totsuka',
 'Lamina espiritual que sela permanentemente tudo que perfura em um genjutsu eterno.',
 'Curto',
 TRUE,
 'Selamento'),

-- Espada Kusanagi (Orochimaru/Sasuke)
('Espada Kusanagi',
 'Espada lendaria extremamente afiada capaz de se estender e conduzir chakra.',
 'Medio',
 TRUE,
 'Arma Lendaria'),

-- Extra pertinente
('Fuuinjutsu Shiki Fuda',
 'Pergaminho especial utilizado para tecnicas de selamento avancadas.',
 'Curto',
 FALSE,
 'Selamento'),

('Pílula Soldado',
 'Comprimido medicinal que restaura rapidamente o chakra do usuario.',
 'Curto',
 FALSE,
 'Cura');
''')

cursor.execute('''
INSERT INTO PersonagensFerramentas (IdPersonagem, IdFerramenta)
SELECT DISTINCT p.IdPersonagem, f.IdFerramenta
FROM Personagens p
JOIN Ferramentas f ON (

    -- 🔹 Ferramentas básicas para TODOS
    f.Nome IN ('Kunai','Shuriken')

    -- 🔹 Papel bomba (todos exceto Haku)
    OR (f.Nome = 'Papel Bomba' 
        AND p.Nome <> 'Haku')

    -- 🔹 Bomba de fumaça (estratégicos)
    OR (f.Nome = 'Bomba de Fumaca'
        AND p.Nome IN (
            'Kakashi','Shikamaru','Asuma',
            'Kurenai','Naruto','Sasuke','Kiba'
        ))

    -- 🔹 Samehada → Kisame
    OR (f.Nome = 'Samehada'
        AND p.Nome = 'Kisame')

    -- 🔹 Kubikiribocho → Zabuza
    OR (f.Nome = 'Kubikiribocho'
        AND p.Nome = 'Zabuza')

    -- 🔹 Espada Kusanagi → Orochimaru e Sasuke
    OR (f.Nome = 'Espada Kusanagi'
        AND p.Nome IN ('Orochimaru','Sasuke'))

    -- 🔹 Espelho de Yata e Espada Totsuka → Itachi
    OR (f.Nome IN ('Espelho de Yata','Espada Totsuka')
        AND p.Nome = 'Itachi')

    -- 🔹 Pilula Soldado → ninjas médicos e Naruto
    OR (f.Nome = 'Pilula Soldado'
        AND p.Nome IN ('Tsunade','Kabuto','Sakura','Naruto'))

    -- 🔹 Fuuinjutsu → Jiraiya, Hiruzen, Orochimaru
    OR (f.Nome = 'Fuuinjutsu Shiki Fuda'
        AND p.Nome IN ('Jiraiya','Hiruzen','Orochimaru'))
)
WHERE p.Nome IN (
'Naruto','Sasuke','Sakura','Kakashi','Kurenai','Kiba','Hinata','Shino',
'Asuma','Shikamaru','Ino','Choji','Might','Rock','Neji','Tenten',
'Baki','Gaara','Kankuro','Temari','Orochimaru','Kabuto','Zabuza',
'Haku','Itachi','Kisame','Kimimaro','Tayuya','Sakon/Ukon',
'Jirobo','Kidomaru','Hiruzen','Jiraiya','Tsunade'
);
''')

conn.commit()