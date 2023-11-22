class NumberProcessor:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def process(self, value):
        print(value)
        return self.data * 2