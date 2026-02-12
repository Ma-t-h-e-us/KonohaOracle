import os
import json
from dotenv import load_dotenv
from openai import OpenAI
import mysql.connector


load_dotenv()

with open("./Protocolos/protocolo.json", "r", encoding="utf-8") as f:
    protocol = json.load(f)

OPENAI_API_KEY=os.getenv("OPEN_API_KEY")

conn = mysql.connector.connect(
    host=os.getenv("host"),
    user=os.getenv("user"),
    port = os.getenv("port"),
    password=os.getenv("password"),
    database=os.getenv("database")
)

cursor = conn.cursor()
cursor.execute('SHOW TABLES')
tabelas = cursor.fetchall()

colunas = {}

for tabela in tabelas :
    cursor.execute(f"DESCRIBE {tabela[0]};")
    colunas_tabelas = cursor.fetchall()
    colunas[tabela[0]] = [coluna[0] for coluna in colunas_tabelas]

cursor.close()
conn.close()

pergunta_usuario = input("Faça sua pergunta: ")

client = OpenAI(api_key=OPENAI_API_KEY)

system_prompt = f"""
Você é um chatbot chamado Konoha Oracle, que realiza consultas SQL em um 
banco de dados (MySql) próprio para responder as perguntas.

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
    max_tokens=200,
    temperature=0
)

# print(response.choices[0].message.content)

query_gerada = response.choices[0].message.content
query_gerada = query_gerada.replace("```sql","").replace("```","")

print(query_gerada)

FORBIDDEN = protocol["forbidden_operations"]

def validate_query(query: str) -> bool:
    q = query.upper()
    if not q.startswith("SELECT"):
        return False
    if any(word in q for word in FORBIDDEN):
        return False
    if ";" in q:
        return False
    if "--" in q or "/*" in q:
        return False
    if "INFORMATION_SCHEMA" in q:
        return False
    return True

if not validate_query(query_gerada):
    print("\n❌ Query bloqueada pelo protocolo de segurança.")
    exit()

try :

    conn = mysql.connector.connect(
        host=str(os.getenv("host")),
        user=str(os.getenv("user")),
        port = int(os.getenv("port")),
        password=str(os.getenv("password")),
        database=str(os.getenv("database"))
    )

    cursor = conn.cursor()
    cursor.execute(query_gerada)
    resultado = cursor.fetchall()

    print(resultado)

    cursor.close()
    conn.close()

except Exception as e:
    print("\nErro ao executar query:")
    print(e)