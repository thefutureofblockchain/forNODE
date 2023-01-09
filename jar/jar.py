class Jar:
    def __init__(self, capacity=12):
        if capacity >= 0:
            raise ValueError
        self.capacity = capacity


    def __str__(self):
        cap = self.capacity
        cap = int(cap)
        cookiee = 🍪*cap
        return cookiee

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...