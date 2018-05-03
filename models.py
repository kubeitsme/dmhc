import config as cfg
import MySQLdb


class StorageEngine(object):
    cursor = ''
    def __init__(self):
        connect = self._connect()
        self.cursor = connect.cursor()

    def _connect(self):
        conn = MySQLdb.connect(host=cfg.DB['host'],
                               user=cfg.DB['user'],
                               passwd=cfg.DB['passwd'],
                               db=cfg.DB['name'],
                               use_unicode=True,
                               charset="utf8")
        return conn
