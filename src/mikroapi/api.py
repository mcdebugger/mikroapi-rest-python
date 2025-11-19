from .client import AsyncMikrotikRESTAPIClient
from .services import InterfaceService, SystemService

class AsyncMikrotikRESTAPI():
    def __init__(self, **kwargs):
        self._client = AsyncMikrotikRESTAPIClient(**kwargs)
        self.interface = InterfaceService(self._client)
        self.system = SystemService(self._client)
    
    async def __aenter__(self):
        await self._client.__aenter__()
        return self
    
    async def __aexit__(self, exc_type, exc_value, traceback):
        await self._client.__aexit__(exc_type, exc_value, traceback)
    
    @property
    def client(self) -> AsyncMikrotikRESTAPIClient:
        """
        Property to access the underlying AsyncMikrotikRESTAPIClient.

        Returns:
            AsyncMikrotikRESTAPIClient: The underlying client.
        """
        return self._client
