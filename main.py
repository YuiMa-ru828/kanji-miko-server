from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import random

app = FastAPI()

KANJI_LIST = [
    {"kanji": "光", "meaning": "light and hope"},
    {"kanji": "空", "meaning": "sky and freedom"},
    {"kanji": "海", "meaning": "ocean and possibility"},
    {"kanji": "星", "meaning": "stars and dreams"},
    {"kanji": "風", "meaning": "wind and change"},
]

@app.post("/kanji")
async def generate_kanji(request: Request):
    data = await request.json()
    name = data.get("name", "Friend")

    kanji_info = random.choice(KANJI_LIST)

    return JSONResponse({
        "messages": [
            {
                "text": f"Thanks, {name}! ✨\nYour Kanji is: 【{kanji_info['kanji']}】\nIt means \"{kanji_info['meaning']}\". 🌟"
            }
        ]
    })
