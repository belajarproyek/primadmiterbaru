from fastapi import APIRouter
from instansis_api import *

router = APIRouter()

@router.post("/instansibyid")
async def view_search_instansis_id(params:dict):
    result = search_instansis_id(**params)
    return result
  
@router.post("/instansibyname")
async def view_search_instansis_by_name(params:dict):
    result = search_instansi_by_name(**params)
    return result

@router.get("/instansis")
async def view_search_instansis_by_name():
    result = search_instansis()
    return result