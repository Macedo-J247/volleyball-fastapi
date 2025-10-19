from fastapi.responses import HTMLResponse
from app import routes
import uvicorn

admin = routes.manager

@admin.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <title> API de Match Making para Vôlei </title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background: #f4f4f4;
                    padding: 20px;
                }

                h1 {
                    color: #2c3e50;  
                }

                .card {
                    background: white;
                    padding: 15px;
                    margin: 10px 0;
                    border-radius: 5px;
                }

                a {
                    text-decoration: none;
                    color: #2980b9;
                }
            </style>
        </head>
        <body>
            <h1> Volleyball Manager V1 </h1>
            <p> [Status] -> Ativa </p>

            <div class="card">
                <h2> Principais endpoints existentes: </h2>
                <ul>
                    <li>
                        <a href="/jogador"> Jogadores </a>
                    </li>
                    <li>
                        <a href="/partida"> Partidas </a>
                    </li>
                    <li>
                        <a href="/avaliacoes"> Avaliações </a>
                    </li>
                </ul>
            </div>

            <div class="card">
                <h2> Documentação da API: </h2>
                <ul>
                    <li>
                        <a href="/docs"> Swagger UI </a>
                    </li>
                    <li>
                        <a href="/redoc"> ReDoc </a>
                    </li>
                </ul>
            </div>
        </body>
    </html>
    """

def main():
    uvicorn.run('main:admin', host='127.0.0.1', port=8000, reload=True)


if __name__ == '__main__':
    main()
