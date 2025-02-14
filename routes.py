from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/users/')
async def get_users(db: Session = Depends(get_db)):
    try:
        return await service.get_users(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/id')
async def get_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(raw_data: schemas.PostUsers, db: Session = Depends(get_db)):
    try:
        return await service.post_users(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/users/id/')
async def put_users_id(raw_data: schemas.PutUsersId, db: Session = Depends(get_db)):
    try:
        return await service.put_users_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/id')
async def delete_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/leads/')
async def get_leads(db: Session = Depends(get_db)):
    try:
        return await service.get_leads(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/leads/id')
async def get_leads_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_leads_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/leads/')
async def post_leads(id: str, created_at: str, name: str, email: str, mobile: str, address: str, city: str, state: str, pincode: str, message: str, source_type: str, company: str, status: str, file_name: UploadFile, db: Session = Depends(get_db)):
    try:
        return await service.post_leads(db, id, created_at, name, email, mobile, address, city, state, pincode, message, source_type, company, status, file_name)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/leads/id/')
async def put_leads_id(raw_data: schemas.PutLeadsId, db: Session = Depends(get_db)):
    try:
        return await service.put_leads_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/leads/id')
async def delete_leads_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_leads_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/admins/')
async def get_admins(db: Session = Depends(get_db)):
    try:
        return await service.get_admins(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/admins/id')
async def get_admins_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_admins_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/admins/')
async def post_admins(raw_data: schemas.PostAdmins, db: Session = Depends(get_db)):
    try:
        return await service.post_admins(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/admins/id/')
async def put_admins_id(raw_data: schemas.PutAdminsId, db: Session = Depends(get_db)):
    try:
        return await service.put_admins_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/admins/id')
async def delete_admins_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_admins_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

