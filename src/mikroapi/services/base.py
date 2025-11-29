from typing import TypeVar, Generic
from ..client import AsyncMikrotikRESTAPIClient
from ..models.base import MikrotikBaseModel

M = TypeVar('M', bound='MikrotikBaseModel')

class BaseService:
    def __init__(self, api: AsyncMikrotikRESTAPIClient):
        self.api = api

class CollectionService(BaseService, Generic[M]):
    def __init__(self, api: AsyncMikrotikRESTAPIClient, endpoint: str, model: type[M]):
        super().__init__(api)
        self.endpoint = endpoint
        self.model = model
    
    async def all(self) -> list[M]:
        data = await self.api.get_list(self.endpoint)
        return [self.model(**item) for item in data]
    
    async def filter(self, **kwargs) -> list[M]:
        data = await self.api.get_list(self.endpoint, filters=kwargs)
        return [self.model(**item) for item in data]
    
    async def get(self, id: str) -> M:
        data = await self.api.get_item(f'{self.endpoint}/{id}')
        return self.model(**data)

class SingleItemService(BaseService, Generic[M]):
    def __init__(self, api: AsyncMikrotikRESTAPIClient, endpoint: str, model: type[M]):
        super().__init__(api)
        self.endpoint = endpoint
        self.model = model
        
    async def get(self) -> M:
        data = await self.api.get_item(self.endpoint)
        return self.model(**data)
