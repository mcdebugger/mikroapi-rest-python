from .base import BaseService, CollectionService, SingleItemService
from ..client import AsyncMikrotikRESTAPIClient
from ..models.system import SystemIdentity, SystemPackage, SystemPackageUpdate
from ..models.system import SystemResource, SystemRouterBoard
from ..models.system import SystemScript

class SystemPackageService(CollectionService[SystemPackage]):
    def __init__(self, api: AsyncMikrotikRESTAPIClient):
        super().__init__(api, 'system/package', SystemPackage)
    
    @property
    def update(self) -> SingleItemService[SystemPackageUpdate]:
        return SingleItemService(self.api, 'system/package/update', SystemPackageUpdate)

class SystemScriptService(CollectionService[SystemScript]):
    def __init__(self, api: AsyncMikrotikRESTAPIClient):
        super().__init__(api, 'system/script', SystemScript)
    
    async def run(self, id: str | None = None, name: str | None = None) -> str:
        if id is None and name is None:
            raise ValueError('Either id or name must be provided')
        params = {'.id': id} if id is not None else {'name': name} if name is not None else {}
        
        response = await self.api.client.post(
            f'{self.api.base_url}/system/script/run',
            json=params
        )
        return self.api._handle_response(response)

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

    @property
    def script(self) -> SystemScriptService:
        return SystemScriptService(self.api)
