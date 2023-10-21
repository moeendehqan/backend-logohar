from mongoengine import Document, StringField, IntField, ListField, DateTimeField, ObjectIdField, FileField,BinaryField, FloatField
import datetime
from persiantools.jdatetime import JalaliDate
from bson import ObjectId
class vector(Document):
    _id = ObjectIdField()
    file = BinaryField(required=True)
    file_name = StringField(required=True)
    file_type = StringField(required=True)
    jobs = ListField(required=True)
    jobs_name = ListField(required=True)
    jobs_name_vector = ListField(required=True)
    keywords = ListField(required=True)
    keywords_vector = ListField(required=True)
    creator = StringField(required=True)
    create_date = DateTimeField(default=datetime.datetime.now())
    aspect_ratio = FloatField(required=True)
    width = IntField(required=True)
    height = IntField(required=True)
    def to_dict(self):
        return {
            '_id': str(self._id),
            'file': self.file,
            'file_name': self.file_name,
            'file_type': self.file_type,
            'jobs': self.jobs,
            'jobs_name': self.jobs_name,
            'keywords': self.keywords,
            'create_date': self.create_date,
            'aspect_ratio':self.aspect_ratio,
            'width':self.width,
            'height':self.height
        }
    @classmethod
    def existing_file(cls, file):
            try:
                res = cls.objects.get(file = file)
                return res != None
            except:
                 return False
    @classmethod
    def tank(cls):
        result = cls.objects.all()
        result = [x.to_dict() for x in result]
        for item in result:
            item['create_date'] = str(JalaliDate.to_jalali(item['create_date'].year,item['create_date'].month,item['create_date'].day))
            item['file'] = item['file'].decode('utf-8')
        return result
    @classmethod
    def delete_vector(cls, id_vector):
        vector_to_delete = cls.objects(_id=ObjectId(id_vector)).delete()
        if vector_to_delete:
            return True
        else:
            return False
        