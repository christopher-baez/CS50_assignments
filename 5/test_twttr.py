from twttr import shorten

def main():
    test_return()
def test_return():
    assert shorten('twitter') == "twttr"
    assert shorten('twitter5') == 'twttr5'
    assert shorten('hello world') == 'hll wrld'
    assert shorten('HELLO') == 'hll'
if __name__ == '__main__':
    main()
