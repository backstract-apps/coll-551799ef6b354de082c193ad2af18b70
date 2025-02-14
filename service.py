from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3

import jwt

import datetime

from pathlib import Path

async def get_users(db: Session):

    users_all = db.query(models.Users).all()
    users_all = [new_data.to_dict() for new_data in users_all] if users_all else users_all

    res = {
        'users_all': users_all,
    }
    return res

async def get_users_id(db: Session, id: int):

    users_one = db.query(models.Users).filter(models.Users.id == id).first() 
    users_one = users_one.to_dict() if users_one else users_one

    res = {
        'users_one': users_one,
    }
    return res

async def post_users(db: Session, raw_data: schemas.PostUsers):
    id:str = raw_data.id
    created_at:str = raw_data.created_at
    name:str = raw_data.name
    email:str = raw_data.email
    password:str = raw_data.password


    record_to_be_added = {'id': id, 'created_at': created_at, 'name': name, 'email': email, 'password': password}
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    users_inserted_record = new_users.to_dict()

    res = {
        'users_inserted_record': users_inserted_record,
    }
    return res

async def put_users_id(db: Session, raw_data: schemas.PutUsersId):
    id:str = raw_data.id
    created_at:str = raw_data.created_at
    name:str = raw_data.name
    email:str = raw_data.email
    password:str = raw_data.password


    users_edited_record = db.query(models.Users).filter(models.Users.id == id).first()
    for key, value in {'id': id, 'created_at': created_at, 'name': name, 'email': email, 'password': password}.items():
          setattr(users_edited_record, key, value)
    db.commit()
    db.refresh(users_edited_record)
    users_edited_record = users_edited_record.to_dict() 

    res = {
        'users_edited_record': users_edited_record,
    }
    return res

async def delete_users_id(db: Session, id: int):

    users_deleted = None
    record_to_delete = db.query(models.Users).filter(models.Users.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete.to_dict() 

    res = {
        'users_deleted': users_deleted,
    }
    return res

async def get_leads(db: Session):

    leads_all = db.query(models.Leads).all()
    leads_all = [new_data.to_dict() for new_data in leads_all] if leads_all else leads_all

    res = {
        'leads_all': leads_all,
    }
    return res

async def get_leads_id(db: Session, id: int):

    leads_one = db.query(models.Leads).filter(models.Leads.id == id).first() 
    leads_one = leads_one.to_dict() if leads_one else leads_one

    res = {
        'leads_one': leads_one,
    }
    return res

async def post_leads(db: Session, id: str, created_at: str, name: str, email: str, mobile: str, address: str, city: str, state: str, pincode: str, message: str, source_type: str, company: str, status: str, file_name: UploadFile):

    
    from datetime import datetime

    try:
        int_id : int = int(id)
        date_created: datetime = datetime.now()
    except Exception as e:
        raise HTTPException(500, str(e))




    id_int: Any = id


    bucket_name = "backstract-testing"
    region_name = "ap-south-1"
    file_path = "resources"

    s3_client = boto3.client(
        's3',
        aws_access_key_id="AKIATET5D5CP6X5H4BNH",
        aws_secret_access_key="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",
        aws_session_token=None,  # Optional, can be removed if not used
        region_name="ap-south-1"
    )

    # Read file content
    file_content = await file_name.read()

    name = file_name.filename
    file_path = file_path  + '/' + name

    import mimetypes
    file_name.file.seek(0)
    s3_client.upload_fileobj(
        file_name.file,
        bucket_name,
        name,
        ExtraArgs={"ContentType": mimetypes.guess_type(name)[0]}

    )

    file_type = Path(file_name.filename).suffix
    file_size = 200

    file_url = f"https://{bucket_name}.s3.amazonaws.com/{name}"

    document = file_url

    record_to_be_added = {'id': int_id, 'created_at': date_created, 'name': name, 'email': email, 'mobile': mobile, 'file_name': document, 'address': address, 'city': city, 'state': state, 'pincode': pincode, 'message': message, 'source_type': source_type, 'company': company, 'status': status}
    new_leads = models.Leads(**record_to_be_added)
    db.add(new_leads)
    db.commit()
    db.refresh(new_leads)
    added_record = new_leads.to_dict()

    res = {
        'rerr': added_record,
    }
    return res

async def put_leads_id(db: Session, raw_data: schemas.PutLeadsId):
    id:str = raw_data.id
    created_at:str = raw_data.created_at
    name:str = raw_data.name
    email:str = raw_data.email
    mobile:str = raw_data.mobile
    attachment:str = raw_data.attachment
    address:str = raw_data.address
    city:str = raw_data.city
    state:str = raw_data.state
    pincode:str = raw_data.pincode
    message:str = raw_data.message


    leads_edited_record = db.query(models.Leads).filter(models.Leads.id == id).first()
    for key, value in {'id': id, 'created_at': created_at, 'name': name, 'email': email, 'mobile': mobile, 'attachment': attachment, 'address': address, 'city': city, 'state': state, 'pincode': pincode, 'message': message}.items():
          setattr(leads_edited_record, key, value)
    db.commit()
    db.refresh(leads_edited_record)
    leads_edited_record = leads_edited_record.to_dict() 

    res = {
        'leads_edited_record': leads_edited_record,
    }
    return res

async def delete_leads_id(db: Session, id: int):

    leads_deleted = None
    record_to_delete = db.query(models.Leads).filter(models.Leads.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        leads_deleted = record_to_delete.to_dict() 

    res = {
        'leads_deleted': leads_deleted,
    }
    return res

async def get_admins(db: Session):

    admins_all = db.query(models.Admins).all()
    admins_all = [new_data.to_dict() for new_data in admins_all] if admins_all else admins_all

    res = {
        'admins_all': admins_all,
    }
    return res

async def get_admins_id(db: Session, id: int):

    admins_one = db.query(models.Admins).filter(models.Admins.id == id).first() 
    admins_one = admins_one.to_dict() if admins_one else admins_one

    res = {
        'admins_one': admins_one,
    }
    return res

async def post_admins(db: Session, raw_data: schemas.PostAdmins):
    id:str = raw_data.id
    created_at:str = raw_data.created_at
    name:str = raw_data.name
    email:str = raw_data.email
    password:str = raw_data.password


    record_to_be_added = {'id': id, 'created_at': created_at, 'name': name, 'email': email, 'password': password}
    new_admins = models.Admins(**record_to_be_added)
    db.add(new_admins)
    db.commit()
    db.refresh(new_admins)
    admins_inserted_record = new_admins.to_dict()

    res = {
        'admins_inserted_record': admins_inserted_record,
    }
    return res

async def put_admins_id(db: Session, raw_data: schemas.PutAdminsId):
    id:str = raw_data.id
    created_at:str = raw_data.created_at
    name:str = raw_data.name
    email:str = raw_data.email
    password:str = raw_data.password


    admins_edited_record = db.query(models.Admins).filter(models.Admins.id == id).first()
    for key, value in {'id': id, 'created_at': created_at, 'name': name, 'email': email, 'password': password}.items():
          setattr(admins_edited_record, key, value)
    db.commit()
    db.refresh(admins_edited_record)
    admins_edited_record = admins_edited_record.to_dict() 

    res = {
        'admins_edited_record': admins_edited_record,
    }
    return res

async def delete_admins_id(db: Session, id: int):

    admins_deleted = None
    record_to_delete = db.query(models.Admins).filter(models.Admins.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        admins_deleted = record_to_delete.to_dict() 

    res = {
        'admins_deleted': admins_deleted,
    }
    return res

