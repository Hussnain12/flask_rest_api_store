from flask import Flask
from flask_smorest import Api
from resources.store import blp as StoreBlueprint
from resources.item import blp as ItemBlueprint

app = Flask(__name__)

# route=app.route()

app.config['PROPOGATE_EXCEPTIONS']=True
app.config['API_TITLE'] = "Stores rest API"
app.config['API_VERSION'] = "v1"
app.config['OPENAPI_VERSION'] = "3.1.0"
app.config['OPENAPI_URL_PREFIX'] = "/"
app.config['OPENAPI_SWAGGER_UI_PATH'] = "/swagger-ui"
app.config['OPENAPI_SWAGGER_UI_URL'] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


api=Api(app)
api.register_blueprint(StoreBlueprint)
api.register_blueprint(ItemBlueprint)

# @app.get("/store")
# def get_all_stores():
#     # return "hello world"
#     return {"stores": list(stores.values())}


# @app.post("/store")
# def create_store():
#     store_data = request.get_json()
#     if "name" not in store_data:
#         abort(400, message="Bad request. Ensure 'name' is included in JSON payload.")
#     for store in stores.values():
#         if store_data["name"] == store["name"]:
#             abort(500, message="Store already Exists")
#     store_id = uuid.uuid4().hex
#     store = {**store_data, "id": store_id}
#     stores[store_id] = store
#     return store, 201


# @app.get("/store/<string:store_id>")
# def get_store(store_id):
#     try:
#         return stores[store_id]
#     except KeyError:
#         abort(404, message="store not found")
        

# @app.delete("/store/<string:store_id>")
# def delete_store(store_id):
#     try:
#         del stores[store_id]
#         return {"message": "store deleted"}
#     except KeyError:
#         abort(404, message="store not found")


# @app.post("/item")
# def create_item():
#     item_data = request.get_json()
#     if (
#         "price" not in item_data or "store_id" not in item_data or "name" not in item_data
#     ):
#         abort(
#             400,
#             message="Bad request, Ensure 'price','store_id','name' are in JSON payload"
#         )
#     for item in items.values():
#         if (
#             item_data["name"] == item["name"] and item_data["store_id"] == item["store_id"]
#         ):
#             abort(500, message="item already exists")
#     if item_data["store_id"] not in stores:
#         abort(404, message="store not found")
#     item_id = uuid.uuid4().hex
#     item = {**item_data, "item_id": item_id}
#     items[item_id] = item
#     return item, 201


# @app.get("/item/<string:item_id>")
# def get_item(item_id):
#     try:
#         return items[item_id]
#     except KeyError:
#         abort(404, message="store not found")

# @app.delete("/item/<string:item_id>")
# def delete_item(item_id):
#     try:
#         del items[item_id]
#         return {"message":"item deleted"}
#     except KeyError:
#         abort(404, message="item not found")

# @app.put("/item/<string:item_id>")
# def update_item(item_id):
#     item_data=request.get_json()
#     if "price" not in item_data or "name" not in item_data:
#         abort(400,message="Bad request, ensure 'price' and 'name' in JSON payload.")
#     try:
#         item=items[item_id]
#         item |= item_data
#         return item
#     except KeyError:
#         abort(404,message="item not found")

# @app.get("/item")
# def get_all_items():
#     return {"items": list(items.values())}
