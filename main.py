from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Msg(BaseModel):
    msg: str


@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}


@app.get("/path")
async def demo_get():
    return {"message": "This is /path endpoint, use a post request to transform the text to uppercase"}


@app.post("/path")
async def demo_post(inp: Msg):
    return {"message": inp.msg.upper()}


@app.get("/path/{path_id}")
async def demo_get_path_id(path_id: int):
    return {"message": f"This is /path/{path_id} endpoint, use post request to retrieve result"}


#uvicorn main:app --reload --host=0.0.0.0 --port=80
if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=80, reload=True, access_log=True, log_config="log.yaml", reload_excludes="api.log" )
    #uvicorn.run('main:app', host="0.0.0.0", port=80, reload=True, access_log=True )
