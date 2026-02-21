import os
import json
import psycopg2
from psycopg2 import OperationalError
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

with open("./Protocolos/protocolo.json", "r", encoding="utf-8") as f:
    protocol = json.load(f)

OPENAI_API_KEY=os.getenv("OPEN_API_KEY")

conn = psycopg2.connect(
    host=os.getenv("host"),
    user=os.getenv("user"),
    port = os.getenv("port"),
    password=os.getenv("password"),
    database=os.getenv("database")
)

cursor = conn.cursor()
cursor.execute('''
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
AND table_type = 'BASE TABLE';
''')
tabelas = cursor.fetchall()

colunas = {}

for tabela in tabelas :
    cursor.execute(f"""
    SELECT column_name
    FROM information_schema.columns
    WHERE table_name = %s
    AND table_schema = 'public';
    """, (tabela[0],))
    colunas_tabelas = cursor.fetchall()
    colunas[tabela[0]] = [coluna[0] for coluna in colunas_tabelas]

cursor.close()
conn.close()

pergunta_usuario = input("Faça sua pergunta: ")

client = OpenAI(api_key=OPENAI_API_KEY)

system_prompt = f"""
Você é um chatbot chamado Konoha Oracle.

Siga rigorosamente o protocolo abaixo:

{json.dumps(protocol, indent=2, ensure_ascii=False)}

Regras adicionais obrigatórias:
- Gere apenas a query SQL pura.
- Nunca use markdown.
- Nunca explique.
"""

user_prompt = f"""

Você deve gerar queries baseadas na seguinte estrutura do banco de dados: {colunas}

Pergunta: {pergunta_usuario}

Resposta em SQL:

"""

response = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    max_tokens=250,
    temperature=0
)

# print(response.choices[0].message.content)

query_gerada = response.choices[0].message.content
query_gerada = query_gerada.replace("```sql","").replace("```","")
query_gerada = query_gerada.strip().rstrip(";")

# print(query_gerada)

FORBIDDEN = protocol["forbidden_operations"]

def validate_query(query: str) -> bool:
    q = query.upper()
    if not q.startswith("SELECT"):
        return False
    if any(word in q for word in FORBIDDEN):
        return False
    if "--" in q or "/*" in q:
        return False
    return True

if not validate_query(query_gerada):
    print("\n Query bloqueada pelo protocolo de segurança.")
    exit()

try :

    conn = psycopg2.connect(
        host=str(os.getenv("host")),
        user=str(os.getenv("user")),
        port = int(os.getenv("port")),
        password=str(os.getenv("password")),
        database=str(os.getenv("database"))
    )

    cursor = conn.cursor()
    cursor.execute(query_gerada)
    resultado = cursor.fetchall()

    # print(resultado)

    cursor.close()
    conn.close()

except Exception as e:
    print("\nErro ao executar query:")
    print(e)

if not resultado:
    print("Não encontrei informações no banco.")
else:
    natural_prompt = f"""
    Você é o Konoha Oracle.

    Baseado exclusivamente nos dados abaixo retornados do banco,
    que segue essa estrutura {colunas},
    responda a pergunta do usuário em linguagem natural.

    Pergunta original:
    {pergunta_usuario}

    Dados retornados:
    {resultado}

    Responda de forma clara, organizada e como um verdadeiro oráculo ninja.
    """

    natural_response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": "Você é o Konoha Oracle. Responda de forma objetiva com base nos dados fornecidos"},
            {"role": "user", "content": natural_prompt}
        ],
        temperature=0.2,
        max_tokens=350
    )

    resposta_final = natural_response.choices[0].message.content
    print("\n🧠 Resposta do Konoha Oracle\n")
    print(resposta_final)