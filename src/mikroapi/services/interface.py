from ..models.interface import Interface, EthernetInterface
from .base import BaseService, CollectionService

class BaseInterfaceService(BaseService):
    pass

class InterfaceService(BaseInterfaceService):
    async def all(self) -> list[Interface]:
        data = await self.api.get_list('interface')
        return [Interface(**interface) for interface in data]
    
    @property
    def ethernet(self):
        return CollectionService(self.api, 'interface/ethernet', EthernetInterface)
