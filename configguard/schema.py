class Field:
    def __init__(self, type, required=False, min=None, max=None):
        self.type = type
        self.required = required
        self.min = min
        self.max = max

class Schema:
    def __init__(self, structure):
        self.structure = structure