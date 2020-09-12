from flask import Blueprint
from controllers import RootController

root: Blueprint = Blueprint('root', __name__)

root.add_url_rule('/', view_func=RootController.as_view('root'), methods=['GET'])
