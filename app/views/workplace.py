from flask import render_template,session,redirect,url_for,current_app
from app import db
from app.models import User,Repository,Product,Equipment
from app.email import send_email
from app.main import main

@main.route('/workplace')
def workplace():
    # 返回设备列表
    rpo_ept_list = []
    transfer_ept_list = []
    machine_ept_list = []
    Equipments = Equipment.query.all()
    for ept in Equipments:
        item = {
            'ept_name': ept.ept_name,
            'status': ept.status,
            'position': ept.position
        }
        if ept.position == '立体仓库':
            rpo_ept_list.append(item)

        elif ept.position == '传送物流':
            transfer_ept_list.append(item)

        elif ept.position == '自动机床':
            machine_ept_list.append(item)
    return render_template('workplace.html',
                            rpo_ept_list = rpo_ept_list, transfer_ept_list = transfer_ept_list, machine_ept_list = machine_ept_list)