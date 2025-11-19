from typing import Any

import httpx

from .exceptions import MikrotikAPIError

class AsyncMikrotikRESTAPIClient:
    def __init__(
        self,
        host: str,
        username: str,
        password: str,
        use_https: bool = True,
        verify_ssl: bool = False,
        timeout: int = 30,
    ):
        self.base_url = f"{'https' if use_https else 'http'}://{host}/rest"
        self.auth = httpx.BasicAuth(username, password)
        self.verify_ssl = verify_ssl
        self.timeout = timeout
    
    async def __aenter__(self):
        self.client = httpx.AsyncClient(
            auth=self.auth,
            verify=self.verify_ssl,
            timeout=self.timeout
        )
        return self
    
    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.client.aclose()

    async def get_list(
        self,
        endpoint: str,
        proplist: list | None = None,
        filters: dict[str, str] | None = None,
    ) -> list[dict[str, Any]]:
        params = {}
        if proplist:
            params['.proplist'] = ','.join(proplist)
        if filters:
            params.update(filters)
        
        response = await self.client.get(
            f'{self.base_url}/{endpoint}',
            auth=self.auth,
            params=params
        )
        return self._handle_response(response)
    
    def _handle_response(self, response: httpx.Response) -> Any:
        if response.status_code >= 400:
            error_data = response.json()
            raise MikrotikAPIError(**error_data)
        
        if response.status_code == 204:
            return None
        
        return response.json()
