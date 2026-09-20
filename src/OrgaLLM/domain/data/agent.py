import logging
from typing import Any, Optional, Literal, List, Dict, Callable
from pydantic import BaseModel, Field
from enum import StrEnum

from .structured_data import StructuredData
from .prompt import Prompt

logger = logging.getLogger(__name__)

class TypeAgent(StrEnum):
    "Liste des types d'assistants disponible"
    LLMECHANGE = "LLMECHANGE"
    LLMStructured = "LLMStructured"

class BaseAgent(BaseModel):
    """Modèle représentant un agent IA simple"""
    type: TypeAgent
    caller: Callable[[str], Dict[str, Any]]
    
    def __init__(self, caller:Callable[[str], Dict[str, Any]]) -> None:
        self.caller: Callable[[str], Dict[str, Any]] = caller
        raise NameError("Do not call this Agent, only children")

    
class LLMAgent(BaseAgent):
    type: TypeAgent = TypeAgent.LLMECHANGE
    prompt:Prompt = Field(..., description="Prompt par défaut de l'assistant")
    
    def __init__(self, prompt:str) -> None:
        self.prompt = Prompt(prompt_system=prompt)
        
    def call(
        self,
        metadata: Dict[str, Any]
    ) -> Dict[str, Any]:
        
        prompt = self.prompt.complete_prompt(**metadata)
        response = self.caller(prompt)
        return response
    
class LLMAgentStructured(LLMAgent):
    type: TypeAgent = TypeAgent.LLMStructured
    parser: StructuredData = Field(..., description="Parser de réponse de l'assistant")