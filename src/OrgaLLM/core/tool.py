from pathlib import Path
import re
from typing import List


def extract_variables(prompt:str) -> List[str]:
    return re.findall(r'\{([a-zA-Z]+[a-zA-Z1-9]*?)\}', prompt)

def if_file_exist(pathfile:str)->bool:
    path = Path(pathfile)
    if path.exists():
        return True
    return False
