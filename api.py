import requests
from pprint import pprint
from tinydb import TinyDB
from tinydb.database import Document
base_url = "https://randomuser.me/api/"

db = TinyDB('data.json',indent=4)
def get_users_by_gender(gender,n):
    params={
        "results":n,
        "gender":gender
    }

    resp=requests.get(base_url,params=params).json()
    return resp

def get_users_for_db(gender,n):
    data=get_users_by_gender(gender,n)
    us=[]
    for i in data["results"]:
        us.append({
            "first_name": i["name"]["first"],
            "last_name": i["name"]["last"],
            "age": i["dob"]["age"],
            "phone": i["phone"],
            "country": i["location"]["country"],
            "email": i["email"],
        })
    return us

users=db.table("males")
pprint(users.insert_multiple(get_users_for_db("females",30)))