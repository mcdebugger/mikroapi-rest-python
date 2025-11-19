from ..models.interface import Interface, EthernetInterface
from .base import BaseService

class BaseInterfaceService(BaseService):
    pass

class EthernetInterfaceService(BaseInterfaceService):
    async def all(self) -> list[EthernetInterface]:
        data = await self.api.get_list('interface/ethernet')
        return [EthernetInterface(**interface) for interface in data]

class InterfaceService(BaseInterfaceService):
    async def all(self) -> list[Interface]:
        data = await self.api.get_list('interface')
        return [Interface(**interface) for interface in data]
    
    @property
    def ethernet(self):
        return EthernetInterfaceService(self.api)
