class A():
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"

    from attribute_tests import A
    x = A()
    x.pub