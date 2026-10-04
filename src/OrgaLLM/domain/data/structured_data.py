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
    TIME = "time"# Time au format HH:mm:ss:ms
    DATETIME = "datetime" # Datetime au format YYYY-MM-DD HH:mm:ss:ms
    LIST = "list"
    DICT = "dict"
    
class StructuredData(BaseModel):
    key: str = Field(..., description="Nom de la donnée")
    value: TypeData = Field(..., description="Type de la colonne (ex: int, str, date)")
    
    def __init__(self, key:str, value:Union[str, TypeData]) -> None:
        self.key = key
        self.value = value if isinstance(value, TypeData) else TypeData(value)
            
class StructuredFormat(BaseModel):
    """Modèle représentant une colonne de table"""
    name: str
    structure: List[Union[StructuredData, StructuredFormat]] = Field(default_factory = List, description="List of all output")
    
    def __init__(self, format:Dict[str, Any]) -> None:
        pass
    
    def get_structure(self) -> List[StructuredData | StructuredFormat]:
        return self.structure
    
    
class ListStructuredFormat(BaseModel):
    structured_formats = List[StructuredFormat]
    
    def __init__(self) -> None:
        self.structured_formats = []
        
    def add_structure(self, format:Dict[str, Any]) -> Union[StructuredData | StructuredFormat]:
        
        name:str = format.get("name", "")
        kind:str = format.get("type", "")
        structure:Dict[str, Any] = format.get("format", {})
        
        if not name:
            raise ValueError("Name not defined")
        
        
        pass