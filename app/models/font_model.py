from mongoengine import Document, StringField, IntField, ListField, DateTimeField, ObjectIdField
import datetime
from persiantools.jdatetime import JalaliDate
from bson import ObjectId

class font(Document):
    _id = ObjectIdField()
    name = StringField(required=True)
    jobs = ListField(required=True)
    jobs_name = ListField(required=True)
    jobs_name_vector = ListField(required=True)
    logo_class = ListField(required=True)
    logo_class_name = ListField(required=True)
    logo_class_name_vector = ListField(required=True)
    file_type = StringField(required=True)
    file_name = StringField(required=True)
    file_name_system = StringField(required=True)
    weight = StringField(required=True)
    file_path = StringField(required=True)
    creator = StringField(required=True)
    create_date = DateTimeField(default=datetime.datetime.now())
    def to_dict(self):
        return {
            '_id': str(self._id),
            'name': self.name,
            'jobs': self.jobs,
            'jobs_name': self.jobs_name,
            'logo_class': self.logo_class,
            'logo_class_name': self.logo_class_name,
            'file_type': self.file_type,
            'file_name': self.file_name,
            'file_name_system': self.file_name_system,
            'weight': self.weight,
            'file_path':self.file_path,
            'create_date':self.create_date,
        }
    @classmethod
    def all(cls):
        all = cls.objects.all()
        result = [item.to_dict() for item in all]
        for item in result:
            item['create_date'] = str(JalaliDate.to_jalali(item['create_date'].year,item['create_date'].month,item['create_date'].day))
        return result
    @classmethod
    def existing(cls,name,weight):
        try:
            result = cls.objects.get(name = name, weight = weight)
            return result != None
        except:
            return False
    @classmethod
    def delete_font(cls, id_font):
        font_to_delete = cls.objects(_id=ObjectId(id_font)).delete()
        if font_to_delete:
            return True
        else:
           return False
        