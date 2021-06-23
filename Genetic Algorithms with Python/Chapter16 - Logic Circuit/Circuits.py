class Not:
    def __init__(self, input):
        self._input = input

    def get_output(self):
        return not self._input.get_output()


class And:
    def __init__(self, inputA, inputB):
        self._inputA = inputA
        self._inputB = inputB

    def get_output(self):
        aValue = self._inputA.get_output()
        bValue = self._inputB.get_output()