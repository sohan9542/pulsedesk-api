from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from pulsedesk_api.config import settings

app = FastAPI(title=settings.app_name)


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok", "env": settings.environment}


@app.websocket("/ws/echo")
async def echo(ws: WebSocket) -> None:
    await ws.accept()
    try:
        while True:
            text = await ws.receive_text()
            await ws.send_text(f"echo: {text}")
    except WebSocketDisconnect:
        pass