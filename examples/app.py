from fastapi import FastAPI
from langcorn import create_service
import uvicorn

app: FastAPI = create_service(
    "examples.lnz:agent"
)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", reload=True, workers=2, port=8000)
   
# pip install chromadb 
# python3.10 examples/app.py
