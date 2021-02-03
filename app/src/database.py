import motor.motor_asyncio

from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.notices

notice_collection = database.get_collection("notices_collection")

def notice_helper(notice) -> dict:
    return {
        "id": str(notice["_id"]),
        "tittle": notice["tittle"],
        "content": notice["content"],
        "date": notice["date"],
    }

# Retrieve all notices present in the database
async def retrieve_notices():
    notices = []
    async for notice in notice_collection.find():
        notices.append(notice_helper(notice))
    return notices


# Add a new notice into to the database
async def add_notice(notice_data: dict) -> dict:
    notice = await notice_collection.insert_one(notice_data)
    new_notice = await notice_collection.find_one({"_id": notice.inserted_id})
    return notice_helper(new_notice)


# Retrieve a notice with a matching ID
async def retrieve_notice(id: str) -> dict:
    notice = await notice_collection.find_one({"_id": ObjectId(id)})
    if notice:
        return notice_helper(notice)


# Update a notice with a matching ID
async def update_notice(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    notice = await notice_collection.find_one({"_id": ObjectId(id)})
    if notice:
        updated_notice = await notice_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_notice:
            return True
        return False


# Delete a notice from the database
async def delete_notice(id: str):
    notice = await notice_collection.find_one({"_id": ObjectId(id)})
    if notice:
        await notice_collection.delete_one({"_id": ObjectId(id)})
        return True