from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def index():
    return {"data": "Hello World"}

@app.get("/blogs")
def blogs(limit: int=10,published: bool=True,sort: Union[str,None]=None):
    if published:
        return {"data": f'showing {limit} published blogs'}
    else:
        return {"data": f'showing {limit} blogs'}

@app.get("/blog/unpublished")
def unpublished():
    return {"data": 'Unpublished blog'}

@app.get("/blog/{blog_id}")
def blog(blog_id: int):
    return {"data": {"blog_id": blog_id}}


# for change the port
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)
