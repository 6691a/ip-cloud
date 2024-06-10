from ipaddress import IPv4Network
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Record(BaseModel):
    id: str
    name: str
    address: IPv4Network


class Action(BaseModel):
    action: str
    record: Record


class WhiteList(BaseModel):
    action: Action
    id: UUID | str = Field(uuid4)
