from main import greet

def test_greet():
    name = "Wee"
    assert greet(name) == f"Hello {name}, Docker is running!!"

