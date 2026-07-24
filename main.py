from fastapi import FastAPI
from fastapi.responses import FileResponse
from kokoro import KPipeline
import soundfile as sf
import uuid

app = FastAPI()

pipeline = KPipeline(lang_code="a")

@app.get("/")
def health():
    return {"status": "ok"}

@app.get("/tts")
def tts(text: str):
    filename = f"{uuid.uuid4()}.wav"

    generator = pipeline(
        text,
        voice="af_heart"
    )

    for _, _, audio in generator:
        sf.write(filename, audio, 24000)
        break

    return FileResponse(
        filename,
        media_type="audio/wav"
    )
