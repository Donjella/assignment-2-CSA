import pytest
from classes.kitchen import Kitchen
from functions.kitchen_functions import add_menu_for_day

@pytest.fixture
def kitchen():
    """Fixture to provide a fresh instance of Kitchen."""
    return Kitchen()

def test_add_menu_for_day(mocker, kitchen):
    # Mock input for week number, day of the week, and meal details
    mocker.patch('builtins.input', side_effect=[
        '1',            # Week number
        '1',            # Day of the week (Monday)
        'Pancakes',     # Breakfast
        'Sandwich',     # Lunch
        'Cookies'       # Afternoon Tea
    ])
    
    # Call `add_menu_for_day` to add a menu to the kitchen
    add_menu_for_day(kitchen)
    
    # Convert week number to string to match the structure of kitchen menu
    week_str = '1'
    
    # Check that the menu was added correctly
    assert week_str in kitchen.menu
    assert 'Monday' in kitchen.menu[week_str]
    assert kitchen.menu[week_str]['Monday']['Breakfast'] == 'Pancakes'
    assert kitchen.menu[week_str]['Monday']['Lunch'] == 'Sandwich'
    assert kitchen.menu[week_str]['Monday']['Afternoon Tea'] == 'Cookies'
