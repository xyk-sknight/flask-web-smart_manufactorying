from flask import render_template,session,redirect,url_for,current_app
from app import db
from app.models import Repository,Product,Equipment,ManufactureTask
from app.main import main
from app.main.forms import RepositoryInputForm,RepositoryOutputForm,TaskAddForm
import time
from app.scripts.rpo_scripts import Rpo_output,Rpo_Input
from app.scripts.rpo_modbus_scrpits import write

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

    # 返回任务列表


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
            write([row,column,0])
        elif state == '入库':
            code = 100*row+10*column+1
            Rpo_Input(rpo_id, proc_id)
            write([row, column, 1])


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