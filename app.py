from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai

# Clé API OpenAI
openai.api_key = "YOUR_OPENAI_API_KEY"

app = FastAPI()

# Modèle de requête
class Query(BaseModel):
    question: str

# Endpoint pour chatbot REST
@app.post("/chat/")
async def chat(query: Query):
    prompt = f"Vous êtes une ressource humaine spécialisée dans les finances. Répondez à la question suivante : {query.question}"
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return {"response": response.choices[0].text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Pour exécuter le serveur
# uvicorn app:app --reload
