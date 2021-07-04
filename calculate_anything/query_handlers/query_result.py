class QueryResult:
    def __init__(self, icon='', value='', name='', description='', is_error=False, clipboard=True, order=-1):
        self.icon = icon
        self.value = value
        self.name = name
        self.description = description
        self.is_error = is_error
        self.clipboard = clipboard
        self.order = order