import gha


def test_reference():
    gha  # pylint: disable=pointless-statement

def test_mypy() -> None:
    def f(x: int):
        pass
    f("")
