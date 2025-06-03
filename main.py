from fastapi import  FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


@app.get("/")
async def root():
    try:
        return {"message": "Hello my world"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 

@app.get("/test")
async def test():
    try:
        return {"message": "welcome to my world"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))