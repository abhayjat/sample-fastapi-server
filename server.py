from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/bhaggus")
async def r_item(name: str, surname: str, roll_no :str):
    print(int(roll_no))
    print(name,surname,roll_no)
    return name+surname+'@gmail.com'+roll_no


uvicorn.run(app,host="192.168.43.35", port=8000, log_level="info")