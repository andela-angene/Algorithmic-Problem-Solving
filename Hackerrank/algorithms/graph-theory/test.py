class foo(object):
    def __init__(self, name, nodes=[]):
        self.name = name
        self.nodes = nodes
        self.distance = float("inf")


a = foo(3)
print(a.name)
