from typing import Optional
from pydantic import BaseModel, Field


class NoticeSchema(BaseModel):
    tittle: str = Field(...)
    content: str = Field(...)
    date: str = Field(...)


    class Config:
        schema_unit = {
            "example":{
                "tittle": "Nova Noticia",
                "content": "Novo conteudo",
                "date": "11/09/2020",
            }
        }


class UpdateNoticeModel(BaseModel):
    tittle: Optional[str]
    content: Optional[str]
    date: Optional[str]


    class Config:
        schema_unit = {
            "example":{
                "tittle": "Nova Noticia",
                "content": "Novo conteudo",
                "date": "11/09/2020",
            }
        }


def ResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}