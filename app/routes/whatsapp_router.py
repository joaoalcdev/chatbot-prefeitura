from fastapi import APIRouter, Form, Request
from fastapi.responses import JSONResponse

whatsapp_router = APIRouter()

@whatsapp_router.post("/webhook")
async def whatsapp_webhook(
    request: Request,
    call_type: str = Form(None),
    call_type_description: str = Form(None),
    call_type_location: str = Form(None),
    call_type_image: str = Form(None),  # Recebendo diretamente via Form
    NumMedia: int = Form(0)
):
    # Se `NumMedia > 0`, então tentamos pegar `MediaUrl0`
    form_data = await request.form()
    media_url = form_data.get("MediaUrl0", call_type_image) if NumMedia > 0 else call_type_image

    print(f"Call Type: {call_type}")
    print(f"Description: {call_type_description}")
    print(f"Location: {call_type_location}")
    print(f"Image URL: {media_url}")

    return JSONResponse(
        content={
            "status": "success",
            "call_type": call_type,
            "description": call_type_description,
            "location": call_type_location,
            "image": media_url
        },
        status_code=200
    )
