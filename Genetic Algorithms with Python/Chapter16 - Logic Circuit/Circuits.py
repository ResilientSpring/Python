class Not:
    def __init__(self, input):
        self._input = input

    def get_output(self):
        if self._input is None:
            return None

        return not self._input.get_output()


class And:
    def __init__(self, inputA, inputB):
        self._inputA = inputA
        self._inputB = inputB

    def get_output(self):
        if self._inputA is None or self._inputB is None:
            return None

        aValue = self._inputA.get_output()
        bValue = self._inputB.get_output()

        return aValue and bValue


class Source:
    def __init__(self, sourceId, sourceContainer):
        self._sourceId = sourceId
        self._sourceContainer = sourceContainer

    def get_output(self):
        return self._sourceContainer[self._sourceId]

