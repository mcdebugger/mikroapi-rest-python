from pydantic import Field

from .base import MikrotikBaseModel

class Interface(MikrotikBaseModel):
    id: str = Field(alias=".id")
    name: str
    type: str
    disabled: bool
    running: bool

class EthernetInterface(MikrotikBaseModel):
    id: str = Field(alias=".id")
    name: str
    disabled: bool
    running: bool
