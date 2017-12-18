

class IntegrationEntry(object):
    def __init__(self, name, deps=[]):
        self.name = name
        self.deps = deps
        self.args = []
        self.url = ""
        self.http_method = ""
        self.response = None

    def run(self):
        pass

    def dump(self):
        """
        dump entry to disk
        """
