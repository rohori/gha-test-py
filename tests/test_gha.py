import gha


def test_reference():
    gha  # pylint: disable=pointless-statement

def test_mypy():
    def f(x: int):
        pass
    f("")
