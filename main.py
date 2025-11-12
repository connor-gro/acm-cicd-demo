from fastapi import FastAPI

from logic import isEven

app = FastAPI()

# A test comment to trigger the workflow
@app.get("/isEven/{num}")
async def root(num: int):
    return {"isEven": isEven(num)}
