from app import routes
import uvicorn

admin = routes.manager

@admin.get("/")
def home():
    return {
        "Mensagem": "API funcional e operante!"
    }

def main():
    uvicorn.run('main:admin', host='127.0.0.1', port=8000, reload=True)


if __name__ == '__main__':
    main()
