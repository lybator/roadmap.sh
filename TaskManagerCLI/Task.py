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
        if self._status == 0:
            return "    Started"
        elif self._status == 1:
            return "In Progress"
        elif self._status > 1:
            return "       Done"

    @status.setter
    def status(self, value):
        self._status = value

    def to_string(self):
        return(f'{self.name + " " + self.status}')

