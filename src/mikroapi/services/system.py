from .base import BaseService, CollectionService, SingleItemService
from ..client import AsyncMikrotikRESTAPIClient
from ..models.system import SystemIdentity, SystemPackage, SystemPackageUpdate
from ..models.system import SystemResource, SystemRouterBoard

class SystemPackageService(CollectionService[SystemPackage]):
    def __init__(self, api: AsyncMikrotikRESTAPIClient):
        super().__init__(api, 'system/package', SystemPackage)
    
    @property
    def update(self) -> SingleItemService[SystemPackageUpdate]:
        return SingleItemService(self.api, 'system/package/update', SystemPackageUpdate)

class SystemService(BaseService):
    @property
    def identity(self) -> SingleItemService[SystemIdentity]:
        return SingleItemService(self.api, 'system/identity', SystemIdentity)

    @property
    def package(self) -> SystemPackageService:
        return SystemPackageService(self.api)
    
    @property
    def resource(self) -> SingleItemService[SystemResource]:
        return SingleItemService(self.api, 'system/resource', SystemResource)

    @property
    def routerboard(self) -> SingleItemService[SystemRouterBoard]:
        return SingleItemService(self.api, 'system/routerboard', SystemRouterBoard)
