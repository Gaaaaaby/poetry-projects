
from utils import FastAPI, Path
from db import teams, users


app = FastAPI()

#search a name 

@app.get("/users/{name}")
async def get_user(name: str = Path(None, description='Type the name of the user you would like to search')):
    userNames = [user["name"] for user in users]

    if name in userNames:
        userIndex = userNames.index(name)
        return 'name of the User:{0}'.format(users[userIndex]['name'])
    else:
        return "Sorry we couldn't find the User"

@app.post("/create-user/{user_id}")
async def create_user(user_id: int, user : users):
    if user_id in users:
        return 'Error the ID already exists'
    users[user_id] = user
    return users[user_id]




    # for team in teams:
    #     if teamName == "Vikings":
    #         return 'members {0}'.format(teams[0]['members'])
    #     elif teamName == "Fighters":
    #         return 'members {0}'.format(teams[1]['members'])
    #     elif teamName == "Cowboys":
    #         return 'members {0}'.format(teams[2]['members'])
    #     else: 
    #         return "couldn't find the team"
