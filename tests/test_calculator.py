from src.calculator import add, subtract, multiply
def test_add():
	assert add(10, 5) == 15

def test_subtract():
	assert subtract(10, 5) == 5

def test_multiply():
	assert multiply(10, 5) == 50
