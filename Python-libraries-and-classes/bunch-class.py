class Bunch(dict):
    def __init__(self, *args, **kwds):
        super(Bunch, self).__init__(*args, **kwds)
        self.__dict__ =self


T = Bunch

t = T(left=T(left="a", right="b"), right=T(left="c"))
print(t.left)
print(t.left.right)