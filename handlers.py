import falcon
import config
import json
import models


class BaseHandler(object):
    def __init__(self, db, table_name):
        self.db = db
        self.table_name = table_name
        self.column_name = self.show_column_name()
    
    def show_column_name(self):
        query = "SHOW columns FROM {0}".format(self.table_name)
        self.db.cursor.execute(query)
        result = [column[0] for column in self.db.cursor.fetchall()]
        return result
    
    def model_to_dict(self, entries):
        dataset = []
        for entry in entries:
            row_data = list(entry)
            _data = {}
            for index, value in enumerate(row_data):
                _data.update({self.column_name[index]: value})
            if _data:
                dataset.append(_data)
        return dataset


class ListHandler(BaseHandler):
    def extract_sort_params(self, params):
        sort_key = params['_sort_key'] if '_sort_key' in params else 'id'
        sort_dir = params['_sort_dir'] if '_sort_dir' in params else 'desc'
        return (sort_key, sort_dir)

    def extract_pager_params(self, params):
        pager_start = int(params['_pager_start']) if '_pager_start' in params else 0
        pager_num = int(params['_pager_num']) if '_pager_num' in params else config.PAGING['page_num']
        return (pager_start, pager_num)

    def build_sort_part(self, query, sort_key, sort_dir):
        query = '{0} ORDER BY {1} {2}'.format(query, sort_key, sort_dir)
        return query

    def get_records(self, query):
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    def GET(self, query, params):
        (sort_key, sort_dir) = self.extract_sort_params(params)
        (pager_start, pager_num) = self.extract_pager_params(params)

        query = self.build_sort_part(query, sort_key, sort_dir)
        dataset = []
        start = pager_start
        end = pager_start + pager_num
        entries = self.get_records(query)
        dataset = self.model_to_dict(entries[start: end])
        total_matched = len(dataset)
        
        resp = {
                'status': 'ok',
                'records': dataset,
                'total_matched': total_matched
            }
        return json.dumps({'data': resp})


class GetHandler(BaseHandler):
    def get_record(self, query):
        self.db.cursor.execute(query)
        return self.db.cursor.fetchone()
    
    def GET(self, params):
        entry = self.get_record(params)
        dataset = []
        if entry:
            dataset = self.model_to_dict((entry, ))
        resp = {
                'status': 'ok',
                'record': dataset,
            }
        return json.dumps({'data': resp})


class GetByHandler(BaseHandler):
    def get_record_by_id(self, query):
        self.db.cursor.execute(query)
        return self.db.cursor.fetchone()
    
    def get_records(self, query):
        pass

    def GET(self, params):
        record_id = int(params[''])


def max_body(limit):
    def hook(req, resp, resouce, params):
        length = req.content_length
        if length is not None and length > limit:
            msg = ('This is of the request is too large.\
                    The body must not exceed \
                    ' + str(limit) + ' bytes in length.')

            raise falcon.HTTPRequestEntityTooLarge(
                'Request body is to large', msg
            )
    
    return hook
