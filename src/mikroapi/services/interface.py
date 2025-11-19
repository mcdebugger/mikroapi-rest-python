from ..models.interface import Interface
from .base import BaseService

class InterfaceService(BaseService):
    async def all(self) -> list[Interface]:
        data = await self.api.get_list('interface')
        return [Interface(**interface) for interface in data]
