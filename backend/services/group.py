from ..models.group import Group
from .. import db

class GroupService:
  @staticmethod
  def insert(data):
    group = Group(
      group_id=data['group_id'],
      name=data['name'],
      group_code=data['group_code'],
      teacher_id=data['teacher_id'],
    )
    db.session.add(group)
    db.session.commit()
    return group