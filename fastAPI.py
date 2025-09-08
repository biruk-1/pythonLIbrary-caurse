from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def root():
    return {"message": "hello world"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("fastAPI:app", host="127.0.0.1", port=8000, reload=True)