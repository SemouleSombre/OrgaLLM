import pytest
from pydantic import ValidationError
from src.OrgaLLM.domain.data.prompt import Prompt, extract_variables

@pytest.mark.parametrize("prompt,expected", [
    ("Extract 0 Variables", []),
    ("Extract 1 {UneSeuleVariable} Variable", ["UneSeuleVariable"]),
    ("{DeuxVariables} Extract 2 Variables {Extraites}", ["DeuxVariables", "Extraites"]),
    ("{A}{B}{C}", ["A", "B", "C"]),
    ("{}", []),
    ("{Var1} {Var2} {Var1}", ["Var1", "Var2"]),
    ("\{Apport\} Journalier", []),
    ("{Avec Espace}", []),
    ("{123quicommenceparchiffres}", [])
])
def test_extract_variables_valid_cases(prompt, expected):
    assert extract_variables(prompt) == expected



@pytest.mark.parametrize("invalid_prompt", [
    None, 
    123, 
    123.45, 
    ["list"], 
    {"dict": "key"}
])

def test_extract_variables_invalid_inputs(invalid_prompt):
    with pytest.raises((TypeError, AttributeError)):  # Selon l'implémentation
        extract_variables(invalid_prompt)

# def test_create_valid_prompt():
#     pass