from src.main import welcome_message


def test_welcome_message():
    assert welcome_message("Ammy") == "Ammy, welcome to the Data Engineering course."


def test_welcome_message_strips_spaces():
    assert welcome_message("  Royce  ") == "Royce, welcome to the Data Engineering course."


def test_empty_name():
    assert welcome_message("   ") == "Welcome to the Data Engineering course."
