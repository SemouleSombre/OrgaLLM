from __future__ import annotations

import logging
from typing import Dict, Any, List, Union
from pydantic import BaseModel
from enum import StrEnum
from pydantic import Field

logger = logging.getLogger(__name__)


class TypeData(StrEnum):
    BOOL = "bool"
    INT = "int"
    FLOAT = "float"
    STR = "str"
    DATE = "date" # Date au format YYYY-MM-DD
    TIME = "time" # Time au format HH:mm:ss:ms
    DATETIME = "datetime" # Datetime au format YYYY-MM-DD HH:mm:ss:ms
    LIST = "list"
    DICT = "dict"
    CHOIX = "choice"
    
class StructuredData(BaseModel):
    key: str = Field(..., description="Nom de la donnée")
    kind:TypeData = Field(..., description="Type de la donnée")
    value:Any = Field(..., description="Valeur de la donnée sélectionnée")
    metadata:Dict[str, Any] = Field()
    
class BoolData(StructuredData):
    kind:TypeData = TypeData.BOOL
    value:bool
    
class IntData(StructuredData):
    kind:TypeData = TypeData.INT
    value:int
    
class FloatData(StructuredData):
    kind:TypeData = TypeData.FLOAT
    value:float
    
class StrData(StructuredData):
    kind:TypeData = TypeData.STR
    value:str
    
class DateData(StructuredData):
    kind:TypeData = TypeData.DATE
    value:str
    
class TimeData(StructuredData):
    kind:TypeData = TypeData.TIME
    value:str
    
class DTData(StructuredData):
    kind:TypeData = TypeData.DATETIME
    value:str

class ChoixData(StructuredData):
    kind:TypeData = TypeData.CHOIX
    value:StructuredData
    choix:List[StructuredData]
    
class ListData(StructuredData):
    kind:TypeData = TypeData.LIST
    value:List[StructuredData]
    elements:List[StructuredData]
    
class DictData(StructuredData):
    kind:TypeData = TypeData.DICT
    value: List[StructuredData]
    format: List[StructuredData]
    
