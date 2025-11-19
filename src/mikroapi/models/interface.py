from typing import Literal
from pydantic import Field

from .base import MikrotikBaseModel

class BaseInterface(MikrotikBaseModel):
    id: str = Field(alias='.id')
    name: str
    comment: str | None = None
    disabled: bool
    mtu: int | Literal['auto']
    running: bool

class Interface(BaseInterface):
    actual_mtu: int
    type: str

class EthernetInterface(BaseInterface):
    pass
