import pytest
from pydantic import ValidationError
from src.OrgaLLM.domain.data.prompt import Prompt, extract_variables

@pytest.mark.parametrize("prompt,expected", [
    ("Extract 0 Variables", []),
    ("Extract 1 {UneSeuleVariable} Variable", ["UneSeuleVariable"]),
    ("{DeuxVariables} Extract 2 Variables {Extraites}", ["DeuxVariables", "Extraites"]),
    ("{A}{B}{C}", ["A", "B", "C"]),  # Cas avec variables collées
    ("{}", [""]),  # Variable vide (si autorisé)
    ("{Var1} {Var2} {Var1}", ["Var1", "Var2", "Var1"]),  # Variables dupliquées
])
def test_extract_variables_valid_cases(prompt, expected):
    assert extract_variables(prompt) == expected





# def test_create_valid_prompt():
#     pass