from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Users(BaseModel):
    id: int
    created_at: datetime.time
    name: str
    email: str
    password: str


class ReadUsers(BaseModel):
    id: int
    created_at: datetime.time
    name: str
    email: str
    password: str
    class Config:
        from_attributes = True


class Leads(BaseModel):
    id: int
    created_at: datetime.time
    name: str
    email: str
    mobile: str
    file_name: str
    address: str
    city: str
    state: str
    pincode: str
    message: str
    source_type: str
    company: str
    status: str


class ReadLeads(BaseModel):
    id: int
    created_at: datetime.time
    name: str
    email: str
    mobile: str
    file_name: str
    address: str
    city: str
    state: str
    pincode: str
    message: str
    source_type: str
    company: str
    status: str
    class Config:
        from_attributes = True


class Admins(BaseModel):
    id: int
    created_at: datetime.time
    name: str
    email: str
    password: str


class ReadAdmins(BaseModel):
    id: int
    created_at: datetime.time
    name: str
    email: str
    password: str
    class Config:
        from_attributes = True




class PostUsers(BaseModel):
    id: str
    created_at: str
    name: str
    email: str
    password: str

    class Config:
        from_attributes = True



class PutUsersId(BaseModel):
    id: str
    created_at: str
    name: str
    email: str
    password: str

    class Config:
        from_attributes = True



class PutLeadsId(BaseModel):
    id: str
    created_at: str
    name: str
    email: str
    mobile: str
    attachment: str
    address: str
    city: str
    state: str
    pincode: str
    message: str

    class Config:
        from_attributes = True



class PostAdmins(BaseModel):
    id: str
    created_at: str
    name: str
    email: str
    password: str

    class Config:
        from_attributes = True



class PutAdminsId(BaseModel):
    id: str
    created_at: str
    name: str
    email: str
    password: str

    class Config:
        from_attributes = True

