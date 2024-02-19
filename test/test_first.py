from fastapi import FastAPI, HTTPException
from starlette.testclient import TestClient
import json
import os

app = FastAPI()


@app.get("/jon")
async def jsonc():
    file_path = 'customers.json'
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    with open(file_path, 'r') as file:
        content = json.load(file)
    return content


client = TestClient(app)


def test_jsonc():
    response = client.get("/jon")
    assert response.status_code == 200
