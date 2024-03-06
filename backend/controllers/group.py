from flask import jsonify
from ..services.group import GroupService

class GroupController:
  @staticmethod
  def create_group(data):
    group = GroupService().insert(data)
    return jsonify(group.to_JSON()), 201