from flask import Blueprint

main = Blueprint('main',__name__)

from .import errors
from app.views import index,repository,products,workplace,equipments