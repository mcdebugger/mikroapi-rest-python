class MikrotikAPIError(Exception):
    def __init__(self, error: int, message: str, detail: str | None = None):
        self.error = error
        self.message = message
        self.detail = detail
        super().__init__(f'{error}: {message} – {detail}')

