from flask import Blueprint, request
from ..controllers.group import GroupController

group_bp = Blueprint('group', __name__)

# TODO: Protect this route, only teachers should be able to create groups
@group_bp.route('/', methods=['POST'])
def create_group():
  return GroupController.create_group(request.get_json())