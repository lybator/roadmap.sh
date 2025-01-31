class Task:
    def __init__(self, name):
        self.name = name
        self.status = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def status(self):
       return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def to_string(self):
        print(f'{self.name + " " + self.status}')

