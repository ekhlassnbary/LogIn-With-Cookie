from fastapi.testclient import TestClient
from main import app
file_path = 'filee/customers.json'
import json
client = TestClient(app)




def test_json():
    response = client.get("/")
    assert response.status_code == 200

def test_jsonc():
    response = client.get("/json")
    assert response.status_code == 200



    # with open(file_path, 'r') as file:
    #     content = file.read()
    #
    # assert response.json() ==json.loads(content)

