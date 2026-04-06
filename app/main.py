from fastapi import FastAPI

app = FastAPI(title="InClass LLM Platform")

@app.get("/")
def root():
    return {"ok": True, "message": "API is running"}
