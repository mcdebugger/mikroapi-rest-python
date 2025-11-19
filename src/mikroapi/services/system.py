from .base import BaseService
from ..models.system import SystemResource

class SystemResourceService(BaseService):
    async def get(self) -> SystemResource:
        data = await self.api.get_item('system/resource')
        return SystemResource(**data)

class SystemService(BaseService):
    pass

    @property
    def resource(self):
        return SystemResourceService(self.api)
