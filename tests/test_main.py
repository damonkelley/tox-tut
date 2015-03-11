from tox_tut.main import is_odd, print_me

# this is a really long useless comment that will cause the linter to fail becuase it is longer the 79 chars.

class TestIsOdd:
    def test_one(self):
        assert is_odd(1) is True

    def test_two(self):
        assert is_odd(2) is False

class TestPrintMe:
    def test_print_me(self):
        print_me()
