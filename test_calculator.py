import calculator

def test_add():
    assert calculator.calculate(2, 3, "add") == 5

def test_terminal_output(capsys):
    assert calculator.calculate(10, 2, "multiply") == 20

def test_argument_passing(monkeypatch):
    monkeypatch.setattr("sys.argv", ["calculator.py", "6", "2", "divide"])
    assert calculator.calculate(6, 2, "divide") == 3.0
