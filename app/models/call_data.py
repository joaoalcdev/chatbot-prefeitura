from typing import Optional
from pydantic import BaseModel

class CallData(BaseModel):
    call_type: Optional[str] = None
    call_type_description: Optional[str] = None
    MediaUrl0: Optional[str] = None
    call_type_location: Optional[str] = None
