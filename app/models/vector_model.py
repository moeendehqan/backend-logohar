from mongoengine import Document, StringField, IntField, ListField, DateTimeField, ObjectIdField, FileField,BinaryField, FloatField
import datetime
from persiantools.jdatetime import JalaliDate
from bson import ObjectId
class vector(Document):
    _id = ObjectIdField()
    file = BinaryField(required=True)
    file_str = StringField(required=True)
    file_name = StringField(required=True)
    file_type = StringField(required=True)
    jobs = ListField(required=True)
    jobs_name = ListField(required=True)
    jobs_name_vector = ListField(required=True)
    logo_class = ListField(required=True)
    logo_class_name = ListField(required=True)
    logo_class_name_vector = ListField(required=True)
    keywords = ListField(required=True)
    keywords_vector = ListField(required=True)
    creator = StringField(required=True)
    create_date = DateTimeField(default=datetime.datetime.now())
    aspect_ratio_file = FloatField(required=True)
    width_file = FloatField(required=True)
    height_file = FloatField(required=True)
    aspect_ratio_content = FloatField(required=True)
    height_content = FloatField(required=True)
    width_content = FloatField(required=True)
    def to_dict(self):
        return {
            '_id': str(self._id),
            'file': self.file,
            'file_name': self.file_name,
            'file_type': self.file_type,
            'jobs': self.jobs,
            'jobs_name': self.jobs_name,
            'logo_class': self.logo_class,
            'logo_class_name': self.logo_class_name,
            'keywords': self.keywords,
            'create_date': self.create_date,
            'aspect_ratio_file':self.aspect_ratio_file,
            'width_file':self.width_file,
            'height_file':self.height_file,
            'aspect_ratio_content':self.aspect_ratio_content,
            'height_content':self.height_content,
            'width_content':self.width_content
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
        vector_all = cls.objects.all()
        print(vector_all)
        if len(vector_all) == 0:
             return []
        vector_all = [x.to_dict() for x in vector_all]
        for item in vector_all:
            item['create_date'] = str(JalaliDate.to_jalali(item['create_date'].year,item['create_date'].month,item['create_date'].day))
            item['file'] = item['file'].decode('utf-8')
        return vector_all
    @classmethod
    def delete_vector(cls, id_vector):
        vector_to_delete = cls.objects(_id=ObjectId(id_vector)).delete()
        if vector_to_delete:
            return True
        else:
            return False
        