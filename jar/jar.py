class Jar:
    def __init__(self, capacity=12):
        if capacity <= 0:
            raise ValueError
        self.capacity = capacity
        self.contain = 0


    def __str__(self):
        self.cap = self.contain
        self.cap = int(self.cap)
        self.cookiee = "🍪"*self.cap
        return self.cookiee

    def deposit(self, n):
        self.p = self.contain+n
        if self.capacity < self.p:
            raise ValueError
        self.contain = self.p




    def withdraw(self, n):
        if self.contain - n < 0:
            raise ValueError
        self.contain = self.contain-n
        return self.contain


    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, capacity):
        if capacity >= 0:
            self._capacity = capacity
        else:
            raise ValueError
    @property
    def size(self):
        return self.contain

def main():
    jar = Jar()
    print(jar.capacity)
    jar.deposit(2)
    print(jar.size)
    jar.withdraw(1)
    print(jar.size)
    jar.deposit(11)
    print(jar)
main()