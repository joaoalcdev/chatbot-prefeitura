from fastapi import FastAPI
from routes.whatsapp_router import whatsapp_router
import uvicorn
from app.utils.ngrok_utils import setup_ngrok
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Pega os arquivos da variável de ambiente
DOMAIN = os.getenv("DOMAIN")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

app = FastAPI()

# Registra o router do WhatsApp
app.include_router(whatsapp_router, tags=["WhatsApp"])

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    # Configura o túnel ngrok
    if DOMAIN and AUTH_TOKEN:
        setup_ngrok(domain=DOMAIN, auth_token=AUTH_TOKEN, port=8000)
    else:
        raise ValueError("As variáveis de ambiente DOMAIN e AUTH_TOKEN não estão definidas.")

    # Inicia o servidor FastAPI
    uvicorn.run(app, host="0.0.0.0", port=8000)
