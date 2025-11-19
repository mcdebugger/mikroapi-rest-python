from .base import MikrotikBaseModel

class SystemIdentity(MikrotikBaseModel):
    name: str

class SystemResource(MikrotikBaseModel):
    architecture_name: str
    board_name: str
    build_time: str
    cpu: str
    cpu_count: int
    cpu_frequency: int
    cpu_load: int
    factory_software: str
    free_hdd_space: int
    free_memory: int
    platform: str
    total_hdd_space: int
    total_memory: int
    uptime: str
    version: str
    write_sect_since_reboot: int
    write_sect_total: int

class SystemRouterBoard(MikrotikBaseModel):
    board_name: str
    current_firmware: str
    factory_firmware: str
    firmware_type: str
    model: str
    routerboard: bool
    serial_number: str
    upgrade_firmware: str
