from elasticsearch import Elasticsearch
from error import IndexRequired


class ES2DF(Elasticsearch):
    """docstring for es2df"""

    def __init__(self, host='localhost', port=9200, index=None, query=None, **kwargs):
        """
        Args:
            host: host of elasticsearch to connect to. (Provide array if multiple)
            port: port of elasticsearch to connect to. (Provide array if multiple)
            index: index/alias of elaticsearch to get data from.
            query: DSL/dict/JSON query to get the results.
            limit: 

        """
        self._es_client = Elasticsearch()
        self._index = index
        if query:
            self._query = query
        for arg, val in kwargs.items():
            setattr(self, arg, val)

    def to_df(self,):
        if not self._index:
            raise IndexRequired('')
        if not self._es_client.indices.exists(index=self._index):
            raise IndexRequired('index')
