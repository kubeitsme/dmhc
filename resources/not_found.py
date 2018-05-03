import falcon

class NotFoundResource(object):
    def handle_404(self, req, resp):
        resp.status = falcon.HTTP_400
        body = 'O.O? làm gì vậy? phá hả?'
        body += ' không có url nào giống vậy đâu,'
        body += ' đọc tài liệu lại đi pa ơi'
        resp.body = (body.encode('utf8'))
