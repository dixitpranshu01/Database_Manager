from fastapi import APIRouter
from models.user import User
from config.database import connection
from schemas.user import userEntity, listOfUserEntity
from bson import ObjectId

user_router = APIRouter()


# creating a password
@user_router.post('/user')
async def save_data(data: User):
    connection.local.User.insert_one(dict(data))
    return listOfUserEntity(connection.local.User.find())


# get one user with matching id
@user_router.get('/user/{userId}')
async def find_person_by_Id(userId):
    return userEntity(connection.local.User.find_one({"_id": ObjectId(userId)}))


# updating a password
@user_router.put('/user/{userId}')
async def update_data(userId, data: User):
    connection.local.User.find_one_and_update(
        {"_id": ObjectId(userId)},
        {"$set": dict(data)}
    )
    return userEntity(connection.local.User.find_one({"_id": ObjectId(userId)}))


# delete a password
@user_router.delete('/user/{userId}')
async def delete_data(userId):
    return userEntity(connection.local.User.find_one_and_delete({"_id": ObjectId(userId)}))
