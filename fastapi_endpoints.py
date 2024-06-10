from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
def root():
    return {"message": "reporting is up and running as of Monday 2024-06-10 V2"}


@app.get("/delinquency/{name}")
def delinquency_stats(name: str):
    """Return statistics on the delinquency table."""
    try:
        s = {"name": name, "version": "1.0"}
        return s
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
