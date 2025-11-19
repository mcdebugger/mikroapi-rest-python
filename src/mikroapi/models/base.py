from pydantic import BaseModel

def to_kebab_case(name):
    return name.replace('_', '-')

def to_snake_case(name):
    return name.replace('-', '_')

class MikrotikBaseModel(BaseModel):
    class Config:
        alias_generator = to_kebab_case
        validate_by_name = True
    
    def __json__(self):
        return self.model_dump()
