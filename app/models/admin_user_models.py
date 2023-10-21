from mongoengine import Document, StringField, IntField, ListField, DateTimeField, ObjectIdField
from bson import ObjectId

class admin_user(Document):
    _id = ObjectIdField()
    username = StringField()
    password = StringField()
    name = StringField()
    @classmethod
    def find_by_id_string(cls, id_string):
        try:
            object_id = ObjectId(id_string)
            user = cls.objects.get(_id=object_id).to_dict()
            return user
        except cls.DoesNotExist:
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    @classmethod
    def find_by_username_and_password(cls, object_username, object_password):
        try:
            user = cls.objects.get(username=object_username, password=object_password).to_dict()
            return user
        except cls.DoesNotExist:
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def to_dict(self):
        return {
            '_id': str(self._id),
            'username': self.username,
            'name': self.name,
        }
    def __repr__(self):
        return f'AdminUser({self.username}, {self.name})'
    


