from bank import value

def main():
    test_return_zero()
    test_return_20()
    test_return_100()
def test_return_zero():
    assert value('hello you') == 0
    assert value('hello friend') == 0

def test_return_20():
    assert value('hey girl') == 20
    assert value('hey man') == 20

def test_return_100():
    assert value('wassup') == 100
    assert value('you there') == 100