import json

from saleapp import app
from saleapp.models import Category, Product


def load_categories():
    # with open("data/categories.json", encoding="utf-8") as f:
    #     return json.load(f)
    return Category.query.all()


def load_products(q=None, cate_id=None, page=None):
    # with open("data/product.json", encoding="utf-8") as f:
    #     products = json.load(f)
    #     if q:
    #         products = [p for p in products if p["name"].find(q) >= 0]
    #
    #     if cate_id:
    #         products = [p for p in products if p["cate_id"].__eq__(int(cate_id))]
    # return products

    query = Product.query
    if q:
        query = query.filter(Product.name.contains(q))
    if cate_id:
        query = query.filter(Product.cate_id.__eq__(cate_id))
    if page:
        size = app.config["PAGE_SIZE"]
        start = (int(page) - 1) * size
        query = query.slice(start, start + size)
    return query.all()
def count_product():
    return Product.query.count()

def get_products_byId(id):
    # with open("data/product.json", encoding="utf-8") as f:
    #     products = json.load(f)
    # for p in products:
    #     if p["id"].__eq__(id):
    #         return p
    # return None
    return Product.query.get(id)
if __name__ == "__main__":
    print(load_products())
