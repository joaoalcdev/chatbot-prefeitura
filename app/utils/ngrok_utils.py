import ngrok

def setup_ngrok(domain: str, auth_token: str, port: int = 8000):
    """
    Configura e inicia o túnel ngrok.
    """
    ngrok.set_auth_token(auth_token)  # Configura o token de autenticação
    listener = ngrok.connect(port, hostname=domain)  # Cria o túnel
    print(f"Ngrok iniciado: {listener.url()}")
