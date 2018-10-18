from flask import render_template,session,redirect,url_for,current_app
from app import db
from app.models import User,Repository,Product
from app.email import send_email
from app.main import main


@main.route('/equpiments', methods=['GET', 'POST'])
def equpiment():

    return render_template('equpiments.html')
