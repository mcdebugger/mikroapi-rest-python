from .base import MikrotikBaseModel
from pydantic import Field

class IPFirewallRule(MikrotikBaseModel):
    id: str = Field(alias='.id')
    action: str | None = None
    chain: str
    disabled: bool | None = None
    dynamic: bool
    invalid: bool | None = None
    bytes: int
    comment: str | None = None
    protocol: str | None = None
    dst_address: str | None = None
    dst_address_list: str | None = None
    dst_address_type: str | None = None
    src_address: str | None = None
    src_address_list: str | None = None
    src_address_type: str | None = None
    dst_port: str | None = None
    src_port: str | None = None
    connection_state: str | None = None
    connection_nat_state: str | None = None
    in_interface: str | None = None
    in_interface_list: str | None = None
    out_interface: str | None = None
    out_interface_list: str | None = None
    routing_mark: str | None = None