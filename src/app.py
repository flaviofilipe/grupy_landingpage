from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import httpx
import json

app = FastAPI()

# Configurar o diretório base
BASE_DIR = Path(__file__).resolve().parent

# Configurar templates e arquivos estáticos
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Rota principal que retorna o template index.html"""
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/comunidade", response_class=HTMLResponse)
async def comunidade(request: Request):
    """Rota que exibe os membros da comunidade"""
    try:
        # Carregar dados dos participantes do arquivo JSON
        json_path = BASE_DIR / "data" / "participantes.json"
        with open(json_path, "r", encoding="utf-8") as file:
            membros = json.load(file)
        
        return templates.TemplateResponse(
            "comunidade.html",
            {"request": request, "membros": membros}
        )
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Arquivo de participantes não encontrado")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Erro ao decodificar arquivo JSON")


@app.get("/eventos", response_class=HTMLResponse)
async def eventos(request: Request):
    """Rota para a página de eventos (em desenvolvimento)"""
    return templates.TemplateResponse(
        "em-desenvolvimento.html",
        {
            "request": request,
            "titulo": "Eventos",
            "icone": "📅",
            "icone_label": "calendário representando eventos",
            "descricao": "toda a programação de eventos, meetups, workshops e palestras da comunidade"
        }
    )


@app.get("/projetos", response_class=HTMLResponse)
async def projetos(request: Request):
    """Rota para a página de projetos (em desenvolvimento)"""
    return templates.TemplateResponse(
        "em-desenvolvimento.html",
        {
            "request": request,
            "titulo": "Projetos",
            "icone": "💻",
            "icone_label": "computador representando projetos",
            "descricao": "todos os projetos open source desenvolvidos pelos membros da nossa comunidade"
        }
    )


@app.get("/github/{username}", response_class=HTMLResponse)
async def github_profile(request: Request, username: str):
    """Rota que busca informações de um perfil do GitHub e exibe em um card"""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"https://api.github.com/users/{username}",
                headers={"Accept": "application/vnd.github.v3+json"}
            )
            
            if response.status_code == 404:
                raise HTTPException(status_code=404, detail="Usuário não encontrado no GitHub")
            
            response.raise_for_status()
            user_data = response.json()
            
            return templates.TemplateResponse(
                "github.html",
                {"request": request, "user": user_data}
            )
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=f"Erro ao buscar dados do GitHub: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
