class QueryResult:
    def __init__(self, icon='', name='', description='', clipboard=None, value=None, error=None, order=-1):
        self.icon = icon
        self.name = name
        self.description = description
        self.clipboard = clipboard
        self.value = value
        self.error = error
        self.order = order