from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.theme import Bootstrap4Theme

from saleapp.models import Category, Product
from saleapp import app, db

class MyCategoryView(ModelView):
    column_list = ['name', 'product']
    column_searchable_list = ['name']

class MyIndexView( AdminIndexView):
    @expose('/')
    def index(self) -> str:
        return self.render('admin/index.html')

admin = Admin(app=app, name="SMART SHOP", theme=Bootstrap4Theme(),index_view=MyIndexView())
admin.add_view(MyCategoryView(Category,  db.session))

admin.add_view(ModelView(Product, db.session))