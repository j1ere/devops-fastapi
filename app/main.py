from fastapi import FastAPI

app = FastAPI(title="DevOps FastAPI Demo")

@app.get("/")
def root():
    return {
        "message": "Hello from FastAPI!",
        "environment": "Development"

    }

@app.get("/health")
def health():
    return {
        "status" : "healthy"
    }

