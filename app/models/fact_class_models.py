from mongoengine import Document, StringField, IntField, ListField, DateTimeField, ObjectIdField



class fact_class(Document):
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
    def get_all_class(cls):
        all_class = cls.objects.all()
        result = [item.to_dict() for item in all_class]
        return result
    @classmethod
    def find_by_name(cls, name):
        print(name)
        result =  cls.objects.get(name = name)
        return result.to_dict()
