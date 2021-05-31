import gha


def test_reference():
    gha  # pylint: disable=pointless-statement

def test_pylint():
    def f(x, y):
        return x
    f(1, 2)
