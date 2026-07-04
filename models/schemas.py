from pydantic import BaseModel
from typing import List, Dict, Any


class Requirement(BaseModel):
    objective: str
    entity_type: str
    category: str
    locations: List[str]
    min_capacity: int
    max_delivery_days: int
    requested_results: int
    preferences: Dict[str, Any]