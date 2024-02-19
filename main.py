from fastapi import FastAPI, File, UploadFile, Query
import json
import os

from starlette.responses import HTMLResponse, JSONResponse

from prettytable import PrettyTable

app = FastAPI()


@app.get("/")
async def index():
    return "Ahalan! You can fetch some json by navigating to '/json'"




with open('filee/customers.json', 'r') as file:
        content = json.load(file)



@app.get("/json")
async def jsonc():
    return content




#
# @app.get("/saints")
# async def saints():
#     with open(file_path, 'r') as file:
#         content = file.read()
#     filew=[]
#     for item in json.loads(content):
#         if item.get("occupation", {}).get("isSaint", True):
#             filew.append(item)
#
#     return filew
#
#
#


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)


#
# @app.get("/short-desc")
# async def short_desc():
#
#     with open(file_path, 'r') as file:
#         content = file.read()
#
#     filew=[]
#     for item in json.loads(content):
#             filew.append([item["name"],item["occupation"]])
#     return filew
#
#
# @app.get("/who")
# async def whoname(name: str):
#     with open(file_path, 'r') as file:
#         content = file.read()
#
#     data = json.loads(content)
#
#     for item in data:
#         if item["name"].lower() == name.lower():
#             return item
#
#     return "No such customer"
#
#
#
#
# @app.get("/saints")
# async def saints(isSaint:bool):
#     with open(file_path, 'r') as file:
#         content = file.read()
#     filew=[]
#     for item in json.loads(content):
#         if item["occupation"]["isSaint"]==isSaint:
#             filew.append(item)
#
#     return filew
#
#
#
#
# @app.post("/saints")
# async def saints_(object: dict):
#     with open(file_path, 'w+') as file:
#         content = file.read()
#
#     content.append(object)
#             # file.truncate()
#
#     return data
#
#
#
#
# @app.post("/saints")
# async def saints_(object: dict):
#     with open(file_path, 'w+') as file:
#         content = file.read()
#
#     content.append(object)
#             # file.truncate()
#
#     return data
#
#
#
# # 9
# @app.get("/who")
# async def get_name(name: str = Query(..., min_length=2, max_length=11)):
#     with open(file_path, 'r') as file:
#             content = file.read()
#
#     data = json.loads(content)
#
#     for item in data:
#      if item["name"].lower() == name.lower():
#                 return item
#
#
#
#
#
# # 8
#
# @app.get("/json")
# async def linkable_name():
#     with open(file_path, 'r') as file:
#         content = file.read()
#
#     data = json.loads(content)
#
#     html_content = "<html><body>"
#     for item in data:
#         linked_name = f'<a href="/who?name={item["name"]}">{item["name"]}</a>'
#         item["name"] = linked_name  # Modify the name in the item to be linked
#         item_json = json.dumps(item)
#         html_content += item_json + "<br>"
#     html_content += "</body></html>"
#
#     return HTMLResponse(content=html_content)
#



# 10
# done








