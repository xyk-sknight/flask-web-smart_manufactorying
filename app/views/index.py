from flask import render_template,session,redirect,url_for,current_app
from app import db
from app.models import User,Repository,Product
from app.email import send_email
from app.main import main

@main.route('/', methods=['GET', 'POST'])
def index():
    input_1 = Repository.query.filter_by(type='原料').count()
    input_2 = Repository.query.filter_by(type='成品').count()
    output = Repository.query.filter_by(type='已出库').count()

    return render_template('index.html',input_1 = input_1,input_2=input_2,output=output)