class CssSelector:
    def __init__(self, tag, identity, classes):
        self._tag = tag
        self._identity = identity
        self._classes = classes

    @property
    def tag(self):
        return self._tag

    @property
    def identity(self):
        return self._identity

    @property
    def classes(self):
        return self._classes
