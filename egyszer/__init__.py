"""Base classes.
"""

__version__ = "0.1.0"

class Meta:
    """Metadata of the `egyszer` file.
    """
    def __init__(self):
        pass


class Document:
    def __init__(self):
        self.content = ""
        self.meta = Meta()
        pass


class Egyszer:
    def __init__(self):
        pass

    def readFile(filename):
        pass

    def createFile(filename):
        return Egyszer()

    def write(self):
        pass

    def close(self):
        pass
