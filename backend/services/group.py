from .. import db

class GroupService:
  """   @staticmethod
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
    
    @staticmethod
    def get_all():
      return Group.query.all()
    
    @staticmethod
    def get_by_code(group_code):
      return Group.query.filter_by(group_code=group_code).first()
    
    @staticmethod
    def get(group_id):
      return Group.query.filter_by(group_id=group_id).first()
    
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
      return group.students """