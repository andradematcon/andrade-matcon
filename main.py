from fastapi import FastAPI, Request
import openai
import os

app = FastAPP()

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post(!/webhook")
async def webhook(request: Resquest):
  data = await request.json()
  mensagem = data.get("message", "olá")
  nome = data.get ("nome", "cliente")
  
  resposta = openai.chatcompletion.create(
    model="gpt-4",
    messages=[
      {"role": "system", "content": "você é MAJU" atendente simpática da loja 'ANDRADE MATERIAIS DE CONSTRUÇÃO' em belém do pará. responda como uma pessoa humana."}
      {"role": "user", "content": f"{nome}: {mensagem}"}
    ]
  )

  return {"resposta": resposta[choices"][0]["message"]["content"]}
         
