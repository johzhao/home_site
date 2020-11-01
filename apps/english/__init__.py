from flask import Blueprint

main = Blueprint('english', __name__, url_prefix='/english')

from . import views
