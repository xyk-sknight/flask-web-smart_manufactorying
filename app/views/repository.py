from flask import render_template,session,redirect,url_for,current_app
from app import db
from app.models import Repository,Product,Equipment,ManufactureTask
from app.main import main
from app.main.forms import RepositoryInputForm,RepositoryOutputForm,TaskAddForm
import time


#仓库管理
@main.route('/repository', methods=['GET', 'POST'])
def repository():
    # 库位状态list
    rpo_list = []
    Rpos = Repository.query.all()
    for rpo in Rpos:
        item = {
            'id':rpo.id,
            'type':rpo.type,
            'product_id':rpo.product_id
        }
        rpo_list.append(item)
    # 返回设备列表
    rpo_ept_list = []
    Equipments = Equipment.query.all()
    for ept in Equipments:
        item = {
            'ept_name': ept.ept_name,
            'status': ept.status,
            'position': ept.position
        }
        if ept.position == '立体仓库':
            rpo_ept_list.append(item)
    #定义入库方法
    def Rpo_Input(rpo_id,proc_id):
        product = Product.query.filter_by(id=proc_id).first()
        # 更新仓库数据
        Repository.query.filter_by(id=rpo_id).update({'type': product.type, 'product_id': proc_id})
        # 更新产品数据
        Product.query.filter_by(id=rpo_id).update({'rpo_id': rpo_id, 'status': '在库', 'position': '仓库'})
    # 定义出库方法
    def Rpo_output(rpo_id,proc_id):
        # 更新仓库数据
        Repository.query.filter_by(id=rpo_id).update({'type': '空', 'product_id': None})
        # 更新产品数据
        Product.query.filter_by(id=proc_id).update({'rpo_id': 0, 'status': '已出库', 'position': '工作台'})

    #定义表单
    form_input = RepositoryInputForm()
    #点击提交按钮
    if form_input.validate_on_submit():
        rpo_id = form_input.id.data
        product_id = form_input.product_id.data
        Rpo_Input(rpo_id,product_id)
        return redirect(url_for('.repository'))


    form_output = RepositoryOutputForm()
    if form_output.validate_on_submit():
        rpo_id = form_input.id.data
        product_id = Repository.query.filter_by(id=rpo_id).first().product_id
        Rpo_output(rpo_id,product_id)
        return redirect(url_for('.repository'))


    # 任务表单
    form_task = TaskAddForm()
    if form_task.validate_on_submit():
        proc_id = form_task.proc_id.data
        state = form_task.state.data
        progress = form_task.progress.data
        rpo_id = form_task.rpo_id.data
        row = Repository.query.filter_by(id=rpo_id).first().row
        column = Repository.query.filter_by(id=rpo_id).first().column
        if state == '出库':
            code = 100*row+10*column+0
            Rpo_output(rpo_id,proc_id)
        else:
            code = 100*row+10*column+1
            Rpo_Input(rpo_id, proc_id)


        localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        new_task = ManufactureTask(proc_id=proc_id,state=state,progress=progress,code=code,start_time=localtime)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('.repository'))

    return render_template('repository.html',
                           rpo_list=rpo_list,rpo_ept_list=rpo_ept_list,
                           form_input=form_input,
                           form_output=form_output,
                           form_task=form_task)