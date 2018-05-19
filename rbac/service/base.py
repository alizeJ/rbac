class Permission:
    def __init__(self, codes):
        self.codes = codes

    def list(self):
        return 'list' in self.codes

    def add(self):
        return 'add' in self.codes

    def delete(self):
        return 'delete' in self.codes

    def edit(self):
        return 'edit' in self.codes
