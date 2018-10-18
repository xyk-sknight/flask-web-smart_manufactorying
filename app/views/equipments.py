from flask import render_template,session,redirect,url_for,current_app
from app import db
from app.models import Equipment
from app.email import send_email
from app.main import main
from app.main.forms import EquipmentAddForm


@main.route('/equipments', methods=['GET', 'POST'])
def equipment():
    # 返回设备列表
    rpo_ept_list = []
    transfer_ept_list = []
    machine_ept_list = []
    Equipments = Equipment.query.all()
    for ept in Equipments:
        item = {
             'ept_name':ept.ept_name,
             'status':ept.status,
             'position':ept.position
        }
        if ept.position == '立体仓库':
            rpo_ept_list.append(item)

        elif ept.position == '传送物流':
            transfer_ept_list.append(item)

        elif ept.position == '自动机床':
            machine_ept_list.append(item)


    # 插入数据

    form_add = EquipmentAddForm()
    if form_add.validate_on_submit():
        ept_name =form_add.eqt_name.data
        status = form_add.status.data
        position = form_add.position.data
        if Equipment.query.filter_by(ept_name=ept_name).first() is None:
            ept = Equipment(ept_name=ept_name, status=status, position=position)
            db.session.add(ept)
            db.session.commit()
            return redirect(url_for('.equipment'))



    return render_template('equipments.html',form_add=form_add,
                           rpo_ept_list=rpo_ept_list,transfer_ept_list=transfer_ept_list,machine_ept_list=machine_ept_list)
