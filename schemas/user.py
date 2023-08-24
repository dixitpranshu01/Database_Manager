# schemas help to serialize and also convert mongodb format json to our icon needed

def userEntity(db_item) -> dict:
    return {
        "id": str(db_item["_id"]),
        "name": db_item["person_name"],
        "address": db_item["address"],
        "email": db_item["email"],
        "phone": db_item["phone"],
        "medical": db_item["medical_history"],
        "family": db_item["family_income"],
        "voter": db_item["voter_id"]
    }


def listOfUserEntity(db_item_list) -> list:
    list_user_entity = []
    for item in db_item_list:
        list_user_entity.append(userEntity(item))
    return list_user_entity
