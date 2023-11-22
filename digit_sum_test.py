from digit_sum import main, digit_sum

def test_digit_sum_function():
    assert digit_sum(12345) == 15, "Die Quersumme von 12345 sollte 15 sein"
    assert digit_sum(101010) == 3, "Die Quersumme von 101010 sollte 3 sein"
    assert digit_sum(7) == 7, "Die Quersumme von 7 sollte 7 sein"

def test_main_with_input_12345(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: '12345')
    main()
    captured = capsys.readouterr()
    assert captured.out == "Die Quersumme ist: 15\n"

def test_main_with_input_101010(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: '101010')
    main()
    captured = capsys.readouterr()
    assert captured.out == "Die Quersumme ist: 3\n"

def test_main_with_input_7(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: '7')
    main()
    captured = capsys.readouterr()
    assert captured.out == "Die Quersumme ist: 7\n"