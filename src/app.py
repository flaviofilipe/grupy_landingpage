from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import httpx

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
