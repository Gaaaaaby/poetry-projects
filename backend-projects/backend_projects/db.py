from typing import List
from schemas import ITeam, IUser


teams : List[ITeam] =  [
    ITeam(name= "Front-end Developers", members=5, date_created="12/09/2019", status="Active", list_tasks=["remodernize interface of Project1,add a weather API to Project2"]), 
    ITeam(name="QA Developers",members=3, date_created="30/07/2021", status="Inactive", list_tasks=["test the Binance application,fix the bugs of the Binance application "]),
    ITeam(name="Backend Developers",members=6,date_created= "04/04/2019",status="Active", list_tasks=[])]


users : List[IUser]= [
    IUser(id=1, name= "John",
        lastname= "Doe", age=67,email= "john@gmail.com",
        address="Florida, USA", 
        number="9393993993",status= "active", position="Senior Developer"),
    IUser(id= 2,
        name= "Jane",
        lastname= "Doeieh",
        age= 45, email= "jdoeiet@gmail.com",
        address=" California, USA", number= "0452048688",
        status="inactive", 
        position= "Recruiter")]