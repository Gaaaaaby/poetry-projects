
from utils import FastAPI, Path
from db import teams, users
from schemas import IUser


app = FastAPI()

#search a name 

@app.get("/users/{name}")
async def get_user(name: str = Path(None, description='Type the name of the user you would like to search')):
    userNames = [user.name for user in users]

    if name in userNames:
        userIndex = userNames.index(name)
        return 'name of the User:{0}'.format(users[userIndex].name)
    else:
        return "Sorry we couldn't find the User"

@app.post("/create-user/")
async def create_user(user: IUser ):
    if user in users: 
        print("The user already exists")
    users.append(user)
    return 'The user was created {0}'.format(user)


@app.delete("/delete-user/{user_id}")
async def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return 'The user {0} was sucessfully deleted '.format(user_id)
        else:
            return 'Sorry we couldnt find an user with that id'

@app.put("/edit-user_id/{user_id}")
async def edit_user_name(user_id: int,user_name: str, user_name_to_edit: str):
    for user in users:
        if user.id == user_id:
                user.name = user_name_to_edit
                return 'The user was updated'
        else:
            return 'We couldnt find an user with that id'