class Bug:
    _counter = 0

    def __init__(self):
        Bug._counter += 1
        self.id = self._counter

    def __del__(self):
        Bug._counter -= 1
        print("koniec", self)

    def __str__(self):
        return f'counter: {self._counter}, id: {self.id}'.format(self=self)


bugs = []
for i in range(100):
    bugs.append(Bug())
    print(bugs[-1])
