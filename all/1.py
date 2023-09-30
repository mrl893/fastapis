from fastapi import FastAPI
from typing import Union
from enum import Enum

app = FastAPI()

@app.get("/")
def index():
    return "hello world!"

# @app.get("/blog/all")
# def get_all_blogs():
#   return {"message": "All blogs provided"}

@app.get("/blog/all")
def get_all_blogs(page = 1, page_size: int = None):
    return {"messege": f"All {page_size} blogs on page {page}"}

@app.get("/blog/{id}/comments/{comment_id}")
def get_comment(id: int, comment_id: int, valid: bool = True, username: str = None):
    return {"messege": f"blog_id{id}, comment_id {comment_id}, valid {valid}, username{username}"}


class BlogType(str, Enum):
    short = "short" # = :
    story ="story"
    howto = "howto"


@app.get(f".blog/type/{type}")
def get_blog_type(type: BlogType):
    return {"messege": f"Blog type {type}"}


@app.post(f"/blog/{id}")
def index1(id:int):
    return {"Hi":  f"Blog with id {id}" }

# my appfastapi


#@app.get("/")
#async def root():
 #   return {"message": "hi How are your self?"}

# Path Parameters
#@app.get("/items/{item_id}")
#async def read_item(item_id):
 #   return {"item_id": item_id}


# Path parameters with types
#@app.get("/items/{item_id}")
#async  def read_item(item_id: int):
 #   return {"item_id": item_id} # "item" : 3


# Order matters
# username
#@app.get("/Users/name")
#async def read_user_name():
 #   return {"user_id": "the current user"}

#@app.get("/users/{user_id}")
#async  def read_user(user_id: str):
#    return {"user_id": user_id}

##@app.get("/users")
#async def read_users(): # users2
 #   return ["Rick", "Morty"]

#@app.get("/users")
##   return ["Bean", "Elfo"]

# create class

# class ModelName(str, Enum):    alexnet = "alexnet" resnet = "resnet" lenet = "lenet"

#@app.get("/models.{model_name}")
#async  def get_model(model_name: ModelName):
 #   if model_name is ModelName.alexnet:
  #      return {"model_name": model_name, "message": "Deep Learning fTW?"}
#
 #   if model_name == "lenet":
  #      return {"model_name": model_name, "message": "LecNN all the images"}

   # return  {"model_name": model_name, "message": "have some residuals"}

# /files/{file_path:path}
# Path convertor


#@app.get("/files/{file_path:path}")
#async def read_file(file_path: str):
 #   return {"file_path": file_path}


# Query Parameters

#fake_items_db = [{"item_name": "Foo"},
 #                {"item_name": "Bar"},
  #               {"item_name": "Baz"}]

# S@app.get("/items/")
#async def read_item(skip: int=0, limit: int=100):
 #   return fake_items_db[skip: skip + limit]


# Optional parameters
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None):
    # if q:
        # return {"item_id": item_id, "q": q}
    # return {"item_id": item_id}

# Query Parameters

#@app.get("/items/{item_id}")
#async def read_item(item_id: str, q: str | None = None, short: bool = False):
 #   item = {"item_id": item_id}
  #  if q:
   ##     item.update({"q": q})
    #if not short:
     #   item.update({
     #       "description ": "this is amazing item that has a long descriptions"
     #   })
    #return item

#@app.get("/users/{user_id}/items/{item_id}")
#async def read_user_item(
#        user_id: int, item_id: str, q: str | None = None, short: bool = False
#):
 #   item = {"item_id": item_id, "owner_id": user_id}
  #  if q:
   ##     item.update({"q": q})
    #if not short:
     #   item.update({
      #      "description ": "this is amazing item that has a long descriptions"
      #  })
    # return item

#@app.get("/items/{item_id}")
#async def read_user_item(item_id: str, needy: str):
 #   item = {"item_id": item_id, "needy": needy}
 #   return item

#@app.get("/items/{item_id}")
#async def read_user_item(
#    item_id: str, needy: str, skip: int = 0, limit: int | None = None
#):
 #   item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
  #  return item

