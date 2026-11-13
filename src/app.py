from fastapi import FastAPI

app = FastAPI(
    title= "Enterprise API Gateway",
    version="v0.1.0"
)


@app.get(path="/health")
async def health_check():
    return {"status":"Healthy"}
