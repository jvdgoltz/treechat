from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/chat")
async def send_message(question: str):
    return {"question": question, "answer": "Your question was " + question}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", port=5000, log_level="info")