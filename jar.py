class Jar:
    def __init__(self, capacity=12):
        if capacity <= 0:
            raise ValueError("Capacity needs to be non-zero positive number")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪"*self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Deposit Exceeds Capacity")
        else:
            self._size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Withdrawal exceeds cookies in jar")
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size