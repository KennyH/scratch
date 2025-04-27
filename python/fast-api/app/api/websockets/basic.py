from fastapi import APIRouter, WebSocket

router = APIRouter()

@router.websocket("/echo")
async def websocket_echo(websocket: WebSocket) -> None:
    """
    WebSocket Echo Server.

    Connect to this endpoint and send a text message. 
    The server will reply back with the same message prefixed by "Echo:".

    JavaScript usage example:

        const ws = new WebSocket('ws://localhost:8000/ws/echo');
        ws.onopen = () => ws.send('Hi');
        ws.onmessage = (event) => console.log(event.data);
    """
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Echo: {data}")
