from plates import is_valid
def main():
    test_number_zero()
    start_with_two_letters()
    test_min_and_max_characters()
def test_min_and_max_characters():
    assert is_valid('AA') == True
    assert is_valid('CHRIS') == True
    assert is_valid('a') == False
    assert is_valid('chirstopher') == False

def start_with_two_letters():
    assert is_valid('AA') == True
    assert is_valid('A2') == False

def test_number_zero():
    assert is_valid('cs50') == True
    assert is_valid('cs05') == False

if __name__ == '__main__':
    main()