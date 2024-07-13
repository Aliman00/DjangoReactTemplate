from ninja import NinjaAPI
from pydantic import BaseModel

api = NinjaAPI()

class MessageOut(BaseModel):
    message: str

@api.get("/hello", response=MessageOut)
def hello_world(request):
    return {"message": "Hello, world!"}