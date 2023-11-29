from fuel import convert, gauge

def main():
    test_convert_valid()
    test_convert_invalid()
    test_gauge_full()
    test_gauge_empty()
    test_gauge_percentage()

def test_convert_valid():
    assert convert('1/2') == 0.5
    assert convert('3/4') == 0.75

def test_convert_invalid():
    assert convert('a/b') is None
    assert convert('1/0') is None

def test_gauge_full():
    assert gauge(1.0) == 'F'

def test_gauge_empty():
    assert gauge(0.0) == 'E'

def test_gauge_percentage():
    assert gauge(0.5) == '50%'
    assert gauge(0.25) == '25%'

if __name__ == '__main__':
    main()
