from ..client import AsyncMikrotikRESTAPIClient
from ..models.ip import IPFirewallFilterRule
from .base import BaseService, CollectionService

class IPFirewallService(BaseService):
    @property
    def filter(self):
        return CollectionService(self.api, 'ip/firewall/filter', IPFirewallFilterRule)
    
class IPService(BaseService):
    @property
    def firewall(self) -> IPFirewallService:
        return IPFirewallService(self.api)
