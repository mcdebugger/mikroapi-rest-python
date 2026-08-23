from ..client import AsyncMikrotikRESTAPIClient
from ..models.ip import IPFirewallRule
from .base import BaseService, CollectionService

class IPFirewallService(BaseService):
    @property
    def filter(self):
        return CollectionService(self.api, 'ip/firewall/filter', IPFirewallRule)
    
    @property
    def mangle(self):
        return CollectionService(self.api, 'ip/firewall/mangle', IPFirewallRule)
    
    @property
    def nat(self):
        return CollectionService(self.api, 'ip/firewall/nat', IPFirewallRule)
    
    @property
    def raw(self):
        return CollectionService(self.api, 'ip/firewall/raw', IPFirewallRule)
    
class IPService(BaseService):
    @property
    def firewall(self) -> IPFirewallService:
        return IPFirewallService(self.api)
