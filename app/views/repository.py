from flask import render_template,session,redirect,url_for,current_app
from app import db
from app.models import Repository,Product
from app.main import main
from app.main.forms import RepositoryInputForm,RepositoryOutputForm




#仓库管理
@main.route('/repository', methods=['GET', 'POST'])
def repository():
    rpo_types_list = []#库位状态list
    for i in range(1, 17):
        types = Repository.query.filter_by(id=i).first()
        type = types.type
        rpo_types_list.append(type)


    #定义表单
    form_input = RepositoryInputForm()
    #点击提交按钮
    if form_input.validate_on_submit():
        row = form_input.row.data
        column = form_input.column.data
        rpo_id = (row-1)*4+column
        product_id = form_input.product_id.data
        product = Product.query.filter_by(id=product_id).first()
        #更新仓库数据
        Repository.query.filter_by(row=row,column=column).update({'type':product.type,'product_id':product_id})
        #更新产品数据
        Product.query.filter_by(id=product_id).update({'rpo_id':rpo_id,'status':'在库','position':'仓库'})
        return redirect(url_for('.repository'))


    form_output = RepositoryOutputForm()
    if form_output.validate_on_submit():
        row = form_output.row.data
        column = form_output.column.data
        product_id = Repository.query.filter_by(row=row,column=column).first().product_id
        # 更新仓库数据
        Repository.query.filter_by(row=row, column=column).update({'type': '已出库', 'product_id': None})
        # 更新产品数据
        Product.query.filter_by(id=product_id).update({'rpo_id': 0, 'status': '已出库', 'position': '工作台'})
        return redirect(url_for('.repository'))

    return render_template('repository.html',
                           rpo_status_list=rpo_types_list,
                           form_input=form_input,
                           form_output=form_output)