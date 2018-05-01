import falcon
import handlers


class ListResource(object):
    def __init__(self, db):
        self.db = db

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        handler = handlers.ListHandler(self.db, 'districts')
        body = handler.GET('SELECT * FROM districts', req.params)
        resp.body = (body)


class GetResource(object):
    def __init__(self, db):
        self.db = db

    def on_get(self, req, resp, district_id):
        resp.status = falcon.HTTP_200
        handler = handlers.GetHandler(self.db, 'districts')
        query = 'SELECT * FROM districts WHERE id = {0}'.format(district_id)
        body = handler.GET(query)
        resp.body = (body)
