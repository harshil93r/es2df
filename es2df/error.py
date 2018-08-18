class IndexRequired(Exception):
    """docstring for IndexRequired"""

    def __init__(self, message=None, errors=None):
        super(IndexRequired, self).__init__(message)
        self.errors = errors

    def __str__(self):
        print('message : ', hasattr(self, 'message'))
        return self.message
