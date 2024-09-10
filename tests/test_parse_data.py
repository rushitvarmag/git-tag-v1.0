import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from main import parse_data


@pytest.fixture
def sample_items():
    '''This fucntion returns a sample items to test the parse data function'''
    items = {
        "items": [
            {"title": "Megahna", "subjects": ["srjkdgn"], "field_offices": ["Office1"]},
            {"title": "JRushit", "subjects": ["awrsg"], "field_offices": ["Office2"]}
        ]
    }
    return items

def test_parse_data(sample_items):
    parsed_data = parse_data(sample_items)
    print(parsed_data)
    output = [
        "MegahnaþsrjkdgnþOffice1",
        "JRushitþawrsgþOffice2"
    ]
    assert output is not None
    assert output==parsed_data