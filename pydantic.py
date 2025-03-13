from fastapi import FastAPI

from pydantic import BaseModel, Field, EmailStr, ConfigDict

app = FastAPI()

data = {
    "email": "abc@mail.ru",
    "bio": None,
    "age": 12
}

class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=100)
    age: int = Field(ge=0, le=130)

    model_config = ConfigDict(extra='forbid')


users = []


@app.post('/users')
def create_user(user: UserSchema):  
    users.append(user)
    return {"ok": True, "msg": "user added"}


@app.get('/users')
def get_users()-> list[UserSchema]: 
    return users