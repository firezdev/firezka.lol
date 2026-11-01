from pathlib import Path

from fastapi import FastAPI, Header, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.utils.views import set_view

app = FastAPI()
templates = Jinja2Templates(directory="app/templates/")

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).resolve().parent.parent / "app" / "static"),
    name="static"
)


@app.get("/")
def get(request: Request, ip: str | None = Header(None, alias="X-Real-IP")):
    total, last_24h, last_1w = set_view(ip)
    return templates.TemplateResponse(
        request,
        "index.html",
        {"views_total": total, "views_24h": last_24h, "views_1w": last_1w}
    )


@app.get("/chupep.jpg")
async def chupep():
    return FileResponse("chupep.jpg")
