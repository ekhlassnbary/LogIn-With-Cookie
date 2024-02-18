from fastapi import FastAPI, HTTPException ,Cookie ,Response
import mysql.connector


app = FastAPI()

# Connect to MySQL database
connection = mysql.connector.connect(
    host='localhost',
    database='usersandpass',
    user='root',
    password='root')


@app.get("/LOGIN")
def name(username:str,password:str, response: Response):
        cursor = connection.cursor()
        query = 'SELECT UserId FROM admin WHERE UserId = %s and UserPassword=%s'
        cursor.execute(query, (username,password))
        results = cursor.fetchall()
        cursor.close()

        if results:
            response.set_cookie(key="UserId", value=results[0][0])
            return {"message": "Login successful"}
        else:
            raise HTTPException(status_code=401, detail="Unauthorized")

# app.middleware("http")(name)


# @app.get("/protected")
# async def protected_route():
#     return {"message": "This route is protected"}
#


@app.get("/admin")
def check_admin(UserId: str = Cookie(None)):
    if UserId:
            return {"message": f'You have longed in before ,welcome {UserId}'}
    raise HTTPException(status_code=401, detail="Unauthorized")




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)

