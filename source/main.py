from fastapi import FastAPI

app = FastAPI (
    title="Production Backend"
)

@app.get("/")
def root():
    return {
        "message" : "Backend running"
    }

from source.config.settings.database import engine


@app.get("/health/db")
async def database_health():

    try:
        async with engine.connect() as connection:
            await connection.execute(text("SELECT 1"))

        return {
            "database": "connected"
        }

    except Exception as e:
        return {
            "database": "failed",
            "error": str(e)
        }