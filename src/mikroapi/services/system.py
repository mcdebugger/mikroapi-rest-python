from .base import BaseService
from ..models.system import SystemIdentity, SystemResource, SystemRouterBoard

class SystemIdentityService(BaseService):
    async def get(self) -> SystemIdentity:
        data = await self.api.get_item('system/identity')
        return SystemIdentity(**data)

class SystemResourceService(BaseService):
    async def get(self) -> SystemResource:
        data = await self.api.get_item('system/resource')
        return SystemResource(**data)

class SystemRouterBoardService(BaseService):
    async def get(self) -> SystemRouterBoard:
        data = await self.api.get_item('system/routerboard')
        return SystemRouterBoard(**data)

class SystemService(BaseService):
    pass

    @property
    def identity(self):
        return SystemIdentityService(self.api)
    
    @property
    def resource(self):
        return SystemResourceService(self.api)
    
    @property
    def routerboard(self):
        return SystemRouterBoardService(self.api)
