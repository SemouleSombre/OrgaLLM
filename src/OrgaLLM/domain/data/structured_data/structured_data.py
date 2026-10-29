from __future__ import annotations

import json, yaml
import logging
from typing import Dict, Any, List, Union
from pydantic import BaseModel
from enum import StrEnum
from pydantic import Field

from ....core.tool import if_file_exist

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
    
    @classmethod
    def from_json(cls,
                  input:str) -> "StructuredData":
        if not (isinstance(input, str) 
                and if_file_exist(input)):
            logger.error(f"File {input} does not exist")
            raise ValueError
        
        with open('src/OrgaLLM/domain/data/ex_struct_format.json', 'r') as file:
            json_docs = json.load(file)

        return cls.from_dict(json_docs)
    
    @classmethod
    def from_yaml(cls,
                  input:str) -> "StructuredData":
        if not (isinstance(input, str) 
                and if_file_exist(input)):
            logger.error(f"File {input} does not exist")
            raise ValueError
        
        with open('src/OrgaLLM/domain/data/ex_struct_format.yaml', 'r') as file:
            yaml_docs = yaml.safe_load_all(file)

            yaml_doc = next(yaml_docs)
            return cls.from_dict(yaml_doc)
                
    
    @classmethod
    def from_dict(cls,
                  input:Union[Dict[str, Any],
                              List[Dict[str, Any]]
                              ]) -> "StructuredData":
        
        if isinstance(input, Dict):
            for key, value in input:
                pass
        elif isinstance(input, List):
            pass
        else:
            logger.error(f"Format of {input} not exist")
            raise ValueError
        
        
        me = cls({})
        return me
    
    def __init__(self, input:Dict[str, Any]) -> None:
        pass
    
    
        
    
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
    
