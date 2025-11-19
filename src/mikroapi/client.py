import httpx

class MikrotikRESTAPI:
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
