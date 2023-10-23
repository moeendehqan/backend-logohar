from mongoengine import Document, StringField, IntField, ListField, DateTimeField, ObjectIdField


class fact_jobs(Document):
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
    def get_all(cls):
        all = cls.objects.all()
        result = [item.to_dict() for item in all]
        return result
    @classmethod
    def find_by_name(cls, name):
        return cls.objects.get(name = name).to_dict()



    