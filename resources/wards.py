import falcon
import handlers


class ListResource(object):
    def __init__(self, db):
        self.db = db

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        handler = handlers.ListHandler(self.db, 'wards')
        body = handler.GET('SELECT * FROM wards', req.params)
        resp.body = (body)


class GetResource(object):
    def __init__(self, db):
        self.db = db

    def on_get(self, req, resp, ward_id):
        resp.status = falcon.HTTP_200
        handler = handlers.GetHandler(self.db, 'wards')
        query = 'SELECT * FROM wards WHERE id = {0}'.format(ward_id)
        body = handler.GET(query)
        resp.body = (body)
