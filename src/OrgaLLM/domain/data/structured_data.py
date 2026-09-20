import logging
from typing import Dict, Any, Optional, Union
from pydantic import BaseModel
from enum import StrEnum
from pydantic import Field

logger = logging.getLogger(__name__)


class TypeData(StrEnum):
    BOOL = "bool"
    INT = "int"
    FLOAT = "float"
    STR = "str"
    DATE = "date"
    LIST = "list"
    DICT = "dict"
    

class StructuredData(BaseModel):
    """Modèle représentant une colonne de table"""
    name: str = Field(..., description="Nom de la donnée")
    type: TypeData = Field(..., description="Type de la colonne (ex: int, str, date)")
    # defaut: Optional[str] = Field(default=None, description="Valeur par défaut")
    # regles: Dict[str, Any] = Field(default_factory=dict, description="Règles de validation en lecture")
    # prompt: Optional[str] = Field(default=None, description="UUID de la clé étrangère pour le prompt")
    # optionnel: bool = Field(default=False, description="Indique si la colonne est optionnelle")
    
    def get_name(self) -> str:
        return self.name
    
    def get_type(self) -> TypeData:
        return self.type
    
    def __init__(self, parser:Union[str, Dict[str,str]]) -> None:
        if not parser:
            raise ValueError
        elif type(parser) == str:
            "cas str"
        elif type(parser) == dict:
            "cas dict"
        else:
            raise ValueError