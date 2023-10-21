from mongoengine import Document, StringField, IntField, ListField, DateTimeField, ObjectIdField


class fact_color_type(Document):
    _id = ObjectIdField()
    name = StringField()
    title = StringField()
    vector = ListField()
    def to_dict(self):
        return {
            '_id': str(self._id),
            'name': self.name,
            'title': self.title,
            'vector': self.vector,
        }
    @classmethod
    def get_all_color_type(cls):
        all_color_types = cls.objects.all()
        result = [color_type.to_dict() for color_type in all_color_types]
        return result
    @classmethod
    def find_by_name(cls, name):
        return cls.objects.get(name = name).to_dict()



    