import falcon
import handlers


class ListResource(object):
    def __init__(self, db):
        self.db = db

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        handler = handlers.ListHandler(self.db, 'provinces')
        body = handler.GET('SELECT * FROM provinces', req.params)
        resp.body = (body)


class GetResource(object):
    def __init__(self, db):
        self.db = db

    def on_get(self, req, resp, province_id):
        resp.status = falcon.HTTP_200
        handler = handlers.GetHandler(self.db, 'provinces')
        query = 'SELECT * FROM provinces WHERE id = {0}'.format(province_id)
        body = handler.GET(query)
        resp.body = (body)
