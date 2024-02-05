class Base1(object):
    def __init__(self):
        self.str1 = "Greek"
        print("Base1")
class Base2(object):
    def __init__(self):
        self.str2 = "Geek2"
        print("Base2")
class derived(Base1, Base2):
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        print("derived")
    def printStrs(self):
        print(self.str1,self.str2)
ob = derived()
ob.printStrs()
    