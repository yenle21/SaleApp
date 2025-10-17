from itertools import product

from flask import Flask, render_template, request
import dao
app = Flask(__name__)


@app.route("/")
def index():
    q=request.args.get("q")
    cate_id =request.args.get("cate_id")
    print(q)
    cates = dao.load_categories()
    products = dao.load_products(q=q, cate_id=cate_id)
    return render_template("index.html", cates = cates,products=products)

@app.route("/products/<int:id>")
def details(id):
    return render_template("details-product.html",products = dao.get_products_byId(id))
if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)
