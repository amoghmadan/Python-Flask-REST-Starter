from flask import Blueprint
from controllers import PersonController, PersonIdController

person: Blueprint = Blueprint('person', __name__)

person.add_url_rule('/', view_func=PersonController.as_view('person_root'), methods=['GET', 'POST'])
person.add_url_rule('/<int:id>/', view_func=PersonIdController.as_view('person_root_id'), methods=['GET', 'PUT', 'DELETE'])
