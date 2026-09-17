class DataModel:
    def __init__(self):
        self.data = []

    def add_data(self, item):
        self.data.append(item)

    def get_data(self):
        return self.data[0] if self.data else "No Data Available"

    def clear_data(self):
        self.data.clear()