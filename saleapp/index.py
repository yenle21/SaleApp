import math

from flask import render_template, request
from werkzeug.utils import redirect

import dao
from saleapp import app, login, admin
from flask_login import login_user, LoginManager, current_user , logout_user


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
@app.route("/Dangnhap/", methods=['get', 'post'])
def loginUser():
    if current_user.is_authenticated:
        return redirect('/')
    err_msg =None

    if request.method.__eq__('POST'):
        username = request.form.get("username")
        password = request.form.get("password")

        user = dao.auth_User(username, password)

        if user:
            login_user(user)
            return redirect('/')
        else:
            err_msg = "Tai khoan hoac mat khau khong dung!!!!"

    return render_template("login.html", err_msg = err_msg )
@app.route("/logout")
def logoutUser():
    logout_user()
    return redirect('/Dangnhap')
@login.user_loader
def get_user(id):
    return dao.get_UserbyID(id)
if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)
