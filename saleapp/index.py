import math

from flask import render_template, request
import dao
from saleapp import app


@app.route("/")
def index():
    q=request.args.get("q")
    cate_id =request.args.get("cate_id")
    pages = request.args.get("page")
    print(q)
    cates = dao.load_categories()
    products = dao.load_products(q=q, cate_id=cate_id, page= pages)
    pages = math.ceil(dao.count_product()/app.config["PAGE_SIZE"])
    return render_template("index.html", cates = cates,products=products,pages= pages)

@app.route("/products/<int:id>")
def details(id):
    return render_template("details-product.html",products = dao.get_products_byId(id))
@app.route("/Dangnhap/")
def login():
    cates = dao.load_categories()
    return render_template("login.html",cates = cates)
if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)
