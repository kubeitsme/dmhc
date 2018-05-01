import falcon
import models
from middleware import auth_middleware
from middleware import require_json
from resources import provinces
from resources import districts
from resources import wards


api = falcon.API(middleware=[
    # auth_middleware.AuthMiddleware(),
    require_json.RequireJSON(),
])
db = models.StorageEngine()
api.add_route('/tinh-thanh',    provinces.ListResource(db))
api.add_route('/tinh-thanh/ma-so/{province_id}',    provinces.GetResource(db))
api.add_route('/quan-huyen',    districts.ListResource(db))
api.add_route('/quan-huyen/ma-so/{district_id}',    districts.GetResource(db))
api.add_route('/phuong-xa',    wards.ListResource(db))
api.add_route('/phuong-xa/ma-so/{ward_id}',    wards.GetResource(db))
