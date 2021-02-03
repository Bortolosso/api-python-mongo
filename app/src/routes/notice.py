from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from src.database import (
    add_notice,
    delete_notice,
    retrieve_notice,
    retrieve_notices,
    update_notice,
)
from src.models.schema import (
    ErrorResponseModel,
    ResponseModel,
    NoticeSchema,
    UpdateNoticeModel,
)


router = APIRouter()


@router.post("/", response_description="Notice data added into the database")
async def add_notice_data(notice: NoticeSchema = Body(...)):
    notice = jsonable_encoder(notice)
    new_notice = await add_notice(notice)
    return ResponseModel(new_notice, "Notice added successfully.")


@router.get("/", response_description="Notices retrieved")
async def get_notices():
    notices = await retrieve_notices()
    if notices:
        return ResponseModel(notices, "Notices data retrieved successfully")
    return ResponseModel(notices, "Empty list returned")


@router.get("/{id}", response_description="Notice data retrieved")
async def get_notice_data(id):
    notice = await retrieve_notice(id)
    if notice:
        return ResponseModel(notice, "Notice data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Notice doesn't exist.")

@router.put("/{id}")
async def update_notice_data(id: str, req: UpdateNoticeModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_notice = await update_notice(id, req)
    if updated_notice:
        return ResponseModel(
            "Notice with ID: {} name update is successful".format(id),
            "Notice name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the notice data.",
    )


@router.delete("/{id}", response_description="Notice data deleted from the database")
async def delete_notice_data(id: str):
    deleted_notice = await delete_notice(id)
    if deleted_notice:
        return ResponseModel(
            "Notice with ID: {} removed".format(id), "Notice deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Notice with id {0} doesn't exist".format(id)
    )