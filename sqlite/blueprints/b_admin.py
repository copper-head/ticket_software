from flask import request, Blueprint

admin_blueprint = Blueprint('admin', __name__)



@admin_blueprint.route('/admin/get_users', methods=['GET'])
def get_users():
    raise NotImplementedError()

