import re
import logging
from typing import List, Dict, Any
from pydantic import BaseModel

logger = logging.getLogger(__name__)

def extract_variables(prompt:str) -> List[str]:
    return re.findall(r'\{(.*?)\}', prompt)

class Prompt(BaseModel):
    prompt_system:str
    variables:List[str]
    
    def __init__(self, prompt_system:str) -> None:
        self.prompt_system = prompt_system
        self.variables = extract_variables(prompt=prompt_system)
    
    def get_prompt_system(self) -> str:
        return self.prompt_system
    
    def get_variables(self) -> List[str]:
        return self.variables
    
    def complete_prompt(self, metadata:Dict[str, Any]) -> str:
        
        if not self.variables and not metadata:
            return self.prompt_system
        
        metadata_not_selected = [m for m in metadata if m not in self.variables]
        variable_not_selected = [v for v in self.variables if v not in metadata]
        prompt = f"""self.prompt_system"""

        if metadata_not_selected:
            logger.warning(f"Metadata not found in variables. Added in the end of prompt. Metadata in excedent : {metadata_not_selected}")
            prompt += "\n".join(f"{{{m}}}" for m in metadata_not_selected)
        
        if variable_not_selected:
            logger.warning(f"Variable empty. Will be ignored : {variable_not_selected}")
            for v in variable_not_selected:
                metadata[v] = ""
        
        return prompt
    
    
    
    