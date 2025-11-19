from .base import BaseService, SingleItemService
from ..models.system import SystemIdentity, SystemResource, SystemRouterBoard

class SystemService(BaseService):
    @property
    def identity(self) -> SingleItemService[SystemIdentity]:
        return SingleItemService(self.api, 'system/identity', SystemIdentity)

    @property
    def resource(self) -> SingleItemService[SystemResource]:
        return SingleItemService(self.api, 'system/resource', SystemResource)

    @property
    def routerboard(self) -> SingleItemService[SystemRouterBoard]:
        return SingleItemService(self.api, 'system/routerboard', SystemRouterBoard)
