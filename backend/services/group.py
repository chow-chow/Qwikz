from ..models.qwikzgroup import QWIKZGROUP as Group
from .. import db

class GroupService:
    @staticmethod
    def insert(data):
        
        group = Group(
            GROUP_NAME=data['GROUP_NAME'],
            GROUP_CODE=data['GROUP_CODE'],
            ACCESS_TOKEN=data['ACCESS_TOKEN'],
            TEACHER_ID=data['TEACHER_ID']
        )
  
        db.session.add(group)
        db.session.commit()
        return group.to_JSON()
    
    @staticmethod
    def get_all():
      return Group.query.all()
    
    @staticmethod
    def get_by_code(group_code):
      return Group.query.filter_by(group_code=group_code).first()
    
    @staticmethod
    def get(access_token):
      """Return the QWIKZGROUP_ID by the access token"""
      group = Group.query.filter_by(ACCESS_TOKEN=access_token).first()
      if group:
        return {
          'QWIKZGROUP_ID': group.QWIKZGROUP_ID,
          'TEACHER_ID': group.TEACHER_ID
        }
    
    @staticmethod
    def get_byID(group_id):
      """Return the group by the group_id"""
      return Group.query.filter_by(QWIKZGROUP_ID=group_id).first()
    
    @staticmethod
    def delete(group_id):
      group = GroupService.get(group_id)
      db.session.delete(group)
      db.session.commit()
      return None
    
    @staticmethod
    def update(group_id, data):
      group = GroupService.get(group_id)
      group.name = data['name']
      group.group_code = data['group_code']
      group.teacher_id = data['teacher_id']
      db.session.commit()
      return group
    
    @staticmethod
    def get_students(group_id):
      group = GroupService.get(group_id)
      return group.students