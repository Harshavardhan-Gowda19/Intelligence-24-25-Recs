from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

# Serve static files (like index.html)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Define the data model for incoming questions
class Question(BaseModel):
    question: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Hogwarts Q&A API!"}
# Run the application with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8004)

