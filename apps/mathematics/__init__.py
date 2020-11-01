from flask import Blueprint

main = Blueprint('mathematics', __name__, url_prefix='/mathematics')

from . import views
