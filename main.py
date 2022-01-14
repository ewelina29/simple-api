
from fastapi import FastAPI


app = FastAPI()

@app.get("/", name='Root endpoint', description='My root endpoint')
def root():
    return {"message": "Hello Worldddddd"}
    # return "Hello World"

