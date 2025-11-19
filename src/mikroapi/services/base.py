from ..client import AsyncMikrotikRESTAPIClient

class BaseService:
    def __init__(self, api: AsyncMikrotikRESTAPIClient):
        self.api = api
