from pydantic import BaseModel

class MikrotikBaseModel(BaseModel):
    class Config:
        validate_by_name = True
    
    def __json__(self):
        return self.model_dump()
