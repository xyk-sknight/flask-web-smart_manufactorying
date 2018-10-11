from flask import render_template,session,redirect,url_for,current_app
from app import db
from app.models import Repository,Product
from app.main import main
from app.main.forms import ProductEditForm,ProductAddForm
# 产品跟踪
@main.route('/products', methods=['GET', 'POST'])
def product_page():
    # 返回所有产品列表
    Products = Product.query.all()
    products = []
    for product in Products:
        if product.position=='仓库':
            position = product.position+'No.'+str(product.rpo_id)
        else:
            position = product.position
        item = {
            'id':product.id,
            'order_id':product.order_id,
            'type':product.type,
            'status':product.status,
            'position':position
        }
        products.append(item)
    # 插入数据
    form_add = ProductAddForm()
    if form_add.validate_on_submit():
        id = form_add.id.data
        order_id = form_add.order_id.data
        type = form_add.type.data
        status = form_add.status.data
        position = form_add.position.data
        if Product.query.filter_by(id=id).all() is not None:
            pass
        else:
            product = Product(id=id,order_id=order_id,type=type,status=status,position=position)
            db.session.add(product)
            db.session.commit()
        return redirect(url_for('.product_page'))


    # 修改数据
    form_edit = ProductEditForm()
    if form_edit.validate_on_submit():
        id = form_edit.id.data
        order_id = form_edit.order_id.data
        type = form_edit.type.data
        status = form_edit.status.data
        position = form_edit.position.data
        Product.query.filter_by(id = id).update(
            {
                'order_id': order_id,
                'type':type,
                'status': status,
                'position': position
            }
        )
        return redirect(url_for('.product_page'))



    return render_template('products.html',products=products,
                           form_add=form_add,
                           form_edit=form_edit)
