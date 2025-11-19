from ..client import AsyncMikrotikRESTAPIClient
from ..models.interface import Interface, EthernetInterface
from .base import BaseService, CollectionService

class BaseInterfaceService(BaseService):
    pass

class InterfaceService(CollectionService[Interface], BaseInterfaceService):
    def __init__(self, api: AsyncMikrotikRESTAPIClient):
        super().__init__(api, 'interface', Interface)
    
    @property
    def ethernet(self):
        return CollectionService(self.api, 'interface/ethernet', EthernetInterface)
